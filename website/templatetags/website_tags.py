
# website/templatetags/website_tags.py
from django import template
from django.utils.safestring import mark_safe
from website.models import WebsiteRequest
from blog.models import BlogPost

register = template.Library()

@register.inclusion_tag('website/widgets/stats_widget.html')
def stats_widget():
    """عرض إحصائيات سريعة في أي صفحة"""
    return {
        'total_requests': WebsiteRequest.objects.count(),
        'pending_requests': WebsiteRequest.objects.filter(status='pending').count(),
        'total_posts': BlogPost.objects.filter(is_published=True).count(),
    }

@register.filter
def status_badge(status):
    """تحويل حالة الطلب إلى badge Bootstrap"""
    badges = {
        'pending': 'warning',
        'in_progress': 'info',
        'completed': 'success',
        'cancelled': 'danger',
    }
    badge_class = badges.get(status, 'secondary')
    status_text = {
        'pending': 'قيد المراجعة',
        'in_progress': 'قيد التنفيذ',
        'completed': 'مكتمل',
        'cancelled': 'ملغى',
    }.get(status, status)
    
    return mark_safe(f'<span class="badge bg-{badge_class}">{status_text}</span>')
