# مساعد لإنشاء admin site مخصص
# website/admin_site.py
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class DeepNooranaAdminSite(AdminSite):
    site_title = _('إدارة Deep Noorana')
    site_header = _('لوحة إدارة Deep Noorana')
    index_title = _('مرحباً بك في لوحة الإدارة')

# استبدال admin site الافتراضي
admin.site = DeepNooranaAdminSite(name='deep_noorana_admin')

