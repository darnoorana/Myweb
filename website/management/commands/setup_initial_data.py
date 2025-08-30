# website/management/commands/setup_initial_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from website.models import WebsiteRequest, ContactMessage
from blog.models import BlogPost
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'إعداد البيانات الأولية للموقع'

    def handle(self, *args, **options):
        self.stdout.write('بدء إعداد البيانات الأولية...')
        
        # إنشاء مستخدم admin إذا لم يكن موجوداً
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@deepnoorana.com',
                password='admin123',
                first_name='مدير',
                last_name='النظام'
            )
            self.stdout.write(self.style.SUCCESS('تم إنشاء مستخدم المدير'))
        
        # إنشاء بعض المستخدمين للاختبار
        test_users = [
            {'username': 'ahmed_dev', 'first_name': 'أحمد', 'last_name': 'محمد', 'email': 'ahmed@test.com'},
            {'username': 'sara_writer', 'first_name': 'سارة', 'last_name': 'علي', 'email': 'sara@test.com'},
            {'username': 'omar_tech', 'first_name': 'عمر', 'last_name': 'حسن', 'email': 'omar@test.com'},
        ]
        
        for user_data in test_users:
            if not User.objects.filter(username=user_data['username']).exists():
                user = User.objects.create_user(
                    password='test123',
                    **user_data
                )
                self.stdout.write(f'تم إنشاء المستخدم: {user.username}')
        
        # إنشاء طلبات مواقع تجريبية
        domains = ['real_estate', 'technology', 'education', 'healthcare', 'business']
        statuses = ['pending', 'in_progress', 'completed']
        
        for i in range(10):
            if not WebsiteRequest.objects.filter(website_name=f'موقع تجريبي {i+1}').exists():
                WebsiteRequest.objects.create(
                    website_name=f'موقع تجريبي {i+1}',
                    domain=random.choice(domains),
                    client_name=f'عميل {i+1}',
                    email=f'client{i+1}@test.com',
                    phone=f'+20100123456{i}',
                    whatsapp=f'+20100123456{i}',
                    description=f'وصف تجريبي للموقع رقم {i+1}',
                    status=random.choice(statuses),
                    created_at=datetime.now() - timedelta(days=random.randint(1, 30))
                )
        
        self.stdout.write(self.style.SUCCESS('تم إنشاء طلبات المواقع التجريبية'))
        
        # إنشاء رسائل تواصل تجريبية
        for i in range(15):
            if not ContactMessage.objects.filter(subject=f'موضوع تجريبي {i+1}').exists():
                ContactMessage.objects.create(
                    name=f'مرسل {i+1}',
                    email=f'sender{i+1}@test.com',
                    phone=f'+20100123456{i}',
                    subject=f'موضوع تجريبي {i+1}',
                    message=f'هذه رسالة تجريبية رقم {i+1} لاختبار النظام',
                    is_read=random.choice([True, False]),
                    created_at=datetime.now() - timedelta(days=random.randint(1, 20))
                )
        
        self.stdout.write(self.style.SUCCESS('تم إنشاء رسائل التواصل التجريبية'))
        
        # إنشاء مقالات تجريبية
        users = User.objects.all()
        blog_posts = [
            {
                'title': 'أساسيات تطوير المواقع باستخدام Django',
                'content': '''Django هو إطار عمل ويب مكتوب بلغة Python يتيح للمطورين بناء تطبيقات ويب قوية وآمنة بسرعة.

## لماذا Django؟

1. **السرعة في التطوير**: Django يوفر الكثير من الميزات الجاهزة
2. **الأمان**: حماية تلقائية ضد العديد من الثغرات الأمنية
3. **القابلية للتوسع**: يمكن التعامل مع المشاريع الكبيرة بسهولة

## البداية مع Django

لبدء مشروع Django جديد، استخدم الأمر التالي:

```bash
django-admin startproject myproject
```

هذا سيقوم بإنشاء هيكل أساسي لمشروع Django جديد.''',
                'excerpt': 'تعلم أساسيات تطوير المواقع باستخدام إطار العمل Django المكتوب بلغة Python'
            },
            {
                'title': 'أفضل الممارسات في تصميم واجهات المستخدم',
                'content': '''تصميم واجهة المستخدم عامل مهم جداً في نجاح أي موقع أو تطبيق.

## المبادئ الأساسية

### 1. البساطة
- تجنب التعقيد غير المبرر
- اجعل التنقل واضحاً وسهلاً
- استخدم مساحات بيضاء بفعالية

### 2. الاتساق
- استخدم نفس الألوان والخطوط
- حافظ على تناسق العناصر
- اجعل السلوك متوقعاً

### 3. إمكانية الوصول
- تأكد من دعم قارئات الشاشة
- استخدم تباين ألوان مناسب
- اجعل الموقع قابل للاستخدام بلوحة المفاتيح''',
                'excerpt': 'تعرف على أفضل الممارسات في تصميم واجهات المستخدم لضمان تجربة مستخدم مثالية'
            },
            {
                'title': 'أهمية تحسين محركات البحث (SEO) للمواقع',
                'content': '''تحسين محركات البحث (SEO) ضروري لضمان ظهور موقعك في نتائج البحث.

## العناصر الأساسية للـ SEO

### 1. المحتوى عالي الجودة
المحتوى هو الملك في عالم SEO. يجب أن يكون:
- مفيداً وذا قيمة للقارئ
- أصلياً وغير منسوخ
- محدثاً بانتظام

### 2. الكلمات المفتاحية
- ابحث عن الكلمات المفتاحية المناسبة
- استخدمها بطريقة طبيعية في النص
- تجنب الحشو المفرط

### 3. التحسين التقني
- سرعة تحميل الصفحات
- التجاوب مع الأجهزة المحمولة
- هيكل URL صديق لمحركات البحث''',
                'excerpt': 'دليل شامل لتحسين محركات البحث وزيادة ظهور موقعك في نتائج Google'
            }
        ]
        
        for i, post_data in enumerate(blog_posts):
            if not BlogPost.objects.filter(title=post_data['title']).exists():
                BlogPost.objects.create(
                    author=random.choice(users),
                    views_count=random.randint(50, 500),
                    created_at=datetime.now() - timedelta(days=random.randint(1, 15)),
                    **post_data
                )
        
        self.stdout.write(self.style.SUCCESS('تم إنشاء المقالات التجريبية'))
        self.stdout.write(self.style.SUCCESS('تم إنهاء إعداد البيانات الأولية بنجاح!'))
