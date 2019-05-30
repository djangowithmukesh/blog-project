
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
#Create your Custom Manager

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

# Create your models here.
class Post(models.Model):
    STATUS_CHOICE= (('draft','draft'),('published','published'))
    title= models.CharField(max_length=300)
    slug= models.SlugField(max_length=300,unique_for_date='publish')
    auther = models.ForeignKey(User,related_name='blog_posts', on_delete=models.CASCADE,)
    body = models.TextField()
    publish= models.DateTimeField(default=timezone.now)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    status =models.CharField(max_length=12,choices=STATUS_CHOICE,default='draft')
    objects=CustomManager()
    tags=TaggableManager()
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',args=[self.publish.year,self.publish.month,self.publish.day,self.slug,])

# Model For Comment Section
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comment', on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return 'Commented by {}on{}'.format(self.name,self.post)


















