
# إضافة middleware مخصص للإحصائيات
# website/middleware.py
import time
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache

class StatsMiddleware(MiddlewareMixin):
    """Middleware لحساب إحصائيات الموقع"""
    
    def process_request(self, request):
        request.start_time = time.time()
        
        # عد الزيارات اليومية
        today_key = f"visits_today_{time.strftime('%Y-%m-%d')}"
        cache.set(today_key, cache.get(today_key, 0) + 1, 86400)  # 24 ساعة
        
    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            duration = time.time() - request.start_time
            response['X-Response-Time'] = f"{duration:.3f}s"
            
        return response
