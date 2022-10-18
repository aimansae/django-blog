from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Post)  # almost always like this
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'created_on')
    # You must define search_fields on the related object’s ModelAdmin because the autocomplete search uses it.
    search_fields = ['title', 'content']


@admin.register(Comment)  # almost always like this
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email_address', 'body')
    action = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
