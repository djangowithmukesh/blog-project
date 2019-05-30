from blog.models import Post
from django import template
from django.db.models import Count
register=template.Library()

@register.simple_tag()
def total_post():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_post.html')
def show_latest_post():
    latest_post=Post.objects.order_by('-publish')[:2]
    return {'latest_post':latest_post}







