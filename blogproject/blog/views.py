from django.core.mail import send_mail
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from taggit.models import Tag

from blog.models import Post
from blog.forms import CommentForm

# Create your views here.
def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])

    paginator= Paginator(post_list,2)
    page_number = request.GET.get('page')
    try:
        post_list =paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/post_list.html',{'post_list':post_list,'tag':tag})

def post_detail_view(request,post,year,month,day):
    post=get_object_or_404(Post,slug=post,publish__year=year,publish__month=month,publish__day=day,status='published')
    comment=post.comment.filter(active=True)
    csubmit=False
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'blog/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comment':comment})

# email sending View
from blog.forms import EmailSendFrom
def email_send_view(request,id):
    post= get_object_or_404(Post,id=id,status='published')
    sent = False
    if request.method=="POST":
        form = EmailSendFrom(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            subject= '{}({}) recomand you to read"{}"'.format(cd['name'],cd['email'],post.title)
            url = request.build_absolute_uri(post.get_absolute_url())
            message= "Read post at:\n {}\n\n{}\'s comment\n{}".format(url,cd['name'],cd['comment'])
            send_mail(subject,message,'mukesh@gmail.com',[cd['to']])
            sent=True
    else:
        form = EmailSendFrom()
    return render(request,'blog/sharemail.html',{'form':form,'post':post,'sent':sent})