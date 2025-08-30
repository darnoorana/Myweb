# context processor مخصص
# website/context_processors.py
from django.conf import settings
from django.core.cache import cache

def site_stats(request):
    """إضافة إحصائيات الموقع لجميع القوالب"""
    return {
        'site_stats': {
            'today_visits': cache.get(f"visits_today_{time.strftime('%Y-%m-%d')}", 0),
            'is_debug': settings.DEBUG,
            'site_name': 'Deep Noorana',
        }
    }
