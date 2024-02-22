from django.contrib import admin
from .models import Post, Comment

# Register your models here. make it visisble in the Django adm section
admin.site.register(Post)
admin.site.register(Comment)
