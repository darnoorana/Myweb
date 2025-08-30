#website/models.py
from django.db import models
from django.contrib.auth.models import User

class WebsiteRequest(models.Model):
    DOMAIN_CHOICES = [
        ('real_estate', 'عقارات'),
        ('technology', 'تكنولوجيا'),
        ('education', 'تعليم'),
        ('healthcare', 'صحة'),
        ('business', 'أعمال'),
        ('ecommerce', 'تجارة إلكترونية'),
        ('portfolio', 'معرض أعمال'),
        ('blog', 'مدونة'),
        ('news', 'أخبار'),
        ('restaurant', 'مطعم'),
        ('other', 'أخرى'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'قيد المراجعة'),
        ('in_progress', 'قيد التنفيذ'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغى'),
    ]
    
    website_name = models.CharField(max_length=200, verbose_name='اسم الموقع')
    domain = models.CharField(max_length=50, choices=DOMAIN_CHOICES, verbose_name='مجال الموقع')
    client_name = models.CharField(max_length=100, verbose_name='اسم العميل')
    email = models.EmailField(verbose_name='البريد الإلكتروني')
    phone = models.CharField(max_length=20, verbose_name='رقم الهاتف')
    whatsapp = models.CharField(max_length=20, blank=True, null=True, verbose_name='واتساب')
    telegram = models.CharField(max_length=100, blank=True, null=True, verbose_name='تليجرام')
    description = models.TextField(verbose_name='وصف المشروع')
    additional_requirements = models.TextField(blank=True, null=True, verbose_name='متطلبات إضافية')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='الحالة')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الطلب')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخر تحديث')
    
    class Meta:
        verbose_name = 'طلب موقع'
        verbose_name_plural = 'طلبات المواقع'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.website_name} - {self.client_name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الإلكتروني')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='رقم الهاتف')
    subject = models.CharField(max_length=200, verbose_name='الموضوع')
    message = models.TextField(verbose_name='الرسالة')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإرسال')
    is_read = models.BooleanField(default=False, verbose_name='تمت القراءة')
    
    class Meta:
        verbose_name = 'رسالة تواصل'
        verbose_name_plural = 'رسائل التواصل'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class JobApplication(models.Model):
    EXPERIENCE_CHOICES = [
        ('beginner', 'مبتدئ'),
        ('intermediate', 'متوسط'),
        ('advanced', 'متقدم'),
        ('expert', 'خبير'),
    ]
    
    POSITION_CHOICES = [
        ('frontend', 'مطور واجهات أمامية'),
        ('backend', 'مطور خلفي'),
        ('fullstack', 'مطور شامل'),
        ('mobile', 'مطور تطبيقات جوال'),
        ('ui_ux', 'مصمم واجهات'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الإلكتروني')
    phone = models.CharField(max_length=20, verbose_name='رقم الهاتف')
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, verbose_name='المنصب المرغوب')
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, verbose_name='مستوى الخبرة')
    skills = models.TextField(verbose_name='المهارات التقنية')
    portfolio_url = models.URLField(blank=True, null=True, verbose_name='رابط معرض الأعمال')
    cv_file = models.FileField(upload_to='cvs/', blank=True, null=True, verbose_name='السيرة الذاتية')
    cover_letter = models.TextField(verbose_name='خطاب تغطية')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ التقديم')
    
    class Meta:
        verbose_name = 'طلب توظيف'
        verbose_name_plural = 'طلبات التوظيف'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_position_display()}"


