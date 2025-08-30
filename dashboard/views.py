from django.shortcuts import render

# Create your views here.
# dashboard/views.py
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from website.models import WebsiteRequest, ContactMessage, JobApplication
from blog.models import BlogPost

@staff_member_required
def dashboard(request):
    """لوحة التحكم الرئيسية"""
    # إحصائيات عامة
    total_website_requests = WebsiteRequest.objects.count()
    pending_requests = WebsiteRequest.objects.filter(status='pending').count()
    total_contact_messages = ContactMessage.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    total_job_applications = JobApplication.objects.count()
    total_blog_posts = BlogPost.objects.count()
    
    # طلبات الأسبوع الماضي
    last_week = timezone.now() - timedelta(days=7)
    recent_requests = WebsiteRequest.objects.filter(created_at__gte=last_week).count()
    
    context = {
        'total_website_requests': total_website_requests,
        'pending_requests': pending_requests,
        'total_contact_messages': total_contact_messages,
        'unread_messages': unread_messages,
        'total_job_applications': total_job_applications,
        'total_blog_posts': total_blog_posts,
        'recent_requests': recent_requests,
    }
    
    return render(request, 'dashboard/dashboard.html', context)
