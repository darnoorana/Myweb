# website/admin.py
from django.contrib import admin
from .admin_site import deep_noorana_admin_site
from django.utils.html import format_html
from .models import WebsiteRequest, ContactMessage, JobApplication

@admin.register(WebsiteRequest, site=deep_noorana_admin_site)
class WebsiteRequestAdmin(admin.ModelAdmin):
    list_display = ['website_name', 'client_name', 'get_domain_display', 'status', 'created_at', 'contact_info']
    list_filter = ['status', 'domain', 'created_at']
    search_fields = ['website_name', 'client_name', 'email', 'phone']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('معلومات الموقع', {
            'fields': ('website_name', 'domain', 'description', 'additional_requirements')
        }),
        ('معلومات العميل', {
            'fields': ('client_name', 'email', 'phone', 'whatsapp', 'telegram')
        }),
        ('حالة الطلب', {
            'fields': ('status',)
        }),
        ('التواريخ', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def contact_info(self, obj):
        return format_html(
            '<a href="mailto:{}">{}</a><br><a href="tel:{}">{}</a>',
            obj.email, obj.email, obj.phone, obj.phone
        )
    contact_info.short_description = 'معلومات التواصل'
    
    actions = ['mark_as_pending', 'mark_as_in_progress', 'mark_as_completed']
    
    def mark_as_pending(self, request, queryset):
        queryset.update(status='pending')
    mark_as_pending.short_description = 'تحديد كقيد المراجعة'
    
    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
    mark_as_in_progress.short_description = 'تحديد كقيد التنفيذ'
    
    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = 'تحديد كمكتمل'

@admin.register(ContactMessage, site=deep_noorana_admin_site)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('معلومات المرسل', {
            'fields': ('name', 'email', 'phone')
        }),
        ('الرسالة', {
            'fields': ('subject', 'message')
        }),
        ('الحالة', {
            'fields': ('is_read', 'created_at')
        }),
    )
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = 'تحديد كمقروءة'
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = 'تحديد كغير مقروءة'

@admin.register(JobApplication, site=deep_noorana_admin_site)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'get_position_display', 'get_experience_level_display', 'created_at']
    list_filter = ['position', 'experience_level', 'created_at']
    search_fields = ['name', 'email', 'skills']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('معلومات المتقدم', {
            'fields': ('name', 'email', 'phone')
        }),
        ('معلومات الوظيفة', {
            'fields': ('position', 'experience_level', 'skills', 'portfolio_url', 'cv_file')
        }),
        ('خطاب التغطية', {
            'fields': ('cover_letter',)
        }),
        ('تاريخ التقديم', {
            'fields': ('created_at',)
        }),
    )

