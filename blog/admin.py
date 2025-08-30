
# blog/admin.py
from django.contrib import admin
from .models import BlogPost, Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published', 'views_count', 'created_at']
    list_filter = ['is_published', 'created_at', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at', 'views_count']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('المحتوى', {
            'fields': ('title', 'slug', 'author', 'content', 'excerpt', 'image')
        }),
        ('الإعدادات', {
            'fields': ('is_published',)
        }),
        ('الإحصائيات', {
            'fields': ('views_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # إذا كان هذا مقال جديد
            obj.author = request.user
        super().save_model(request, obj, form, change)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'content_preview', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['content', 'author__username', 'post__title']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'معاينة التعليق'
    
    actions = ['approve_comments', 'disapprove_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = 'الموافقة على التعليقات'
    
    def disapprove_comments(self, request, queryset):
        queryset.update(is_approved=False)
    disapprove_comments.short_description = 'رفض التعليقات'
