# package in Django that contains a collection of reusable Django applications and modules provided by the Django project
from django.contrib import admin

from .models import About
from .models import CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
# to customise the admin panel view in your own projects, then inherit from admin.ModelAdmin

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)    