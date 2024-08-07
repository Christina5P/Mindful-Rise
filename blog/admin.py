from django.contrib import admin
from blog.models import Category, Comment, Post, Courses 
from django_summernote.admin import SummernoteModelAdmin

# Register your models here for administrative interface


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status','created_on')
    search_fields = ['title', 'content']
    list_filter = ('categories',)
    summernote_fields = ('content',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}

    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin panel for comments"""
    list_display = ('post', 'author', 'body', 'created_on', 'approved')
    list_filter = ('created_on', 'approved')
    search_fields = ['author', 'body', 'approved']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        updated_count = queryset.update(approved=True) 
        self.message_user(request, f'{updated_count}Approved comments')
    
    approve_comments.short_description = "Approve comments"
    
@admin.register(Courses)
class CoursesAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_on')  # Ta bort 'slug'
    search_fields = ['title', 'content']
    list_filter = ('categories',)
    summernote_fields = ('content',)
