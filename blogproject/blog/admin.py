from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','auther','body','publish','created','updated','status']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title','body'),
    list_filter = ('status',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','body','created','updated','active']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)