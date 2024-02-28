"""register models with the admin interface

@admin.register(Post) This is a decorator-based approach 



"""

from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('author','title','status','created_on','updated_on')
    search_fields = ['title','content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here. make it visisble in the Django adm section
#@admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','created_on','email','approved')