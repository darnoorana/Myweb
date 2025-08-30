
# Create your models here.
# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='العنوان')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='المؤلف')
    content = models.TextField(verbose_name='المحتوى')
    excerpt = models.TextField(max_length=500, blank=True, null=True, verbose_name='مقتطف')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name='صورة')
    is_published = models.BooleanField(default=True, verbose_name='منشور')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخر تحديث')
    views_count = models.PositiveIntegerField(default=0, verbose_name='عدد المشاهدات')
    
    class Meta:
        verbose_name = 'مقالة'
        verbose_name_plural = 'المقالات'
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='المؤلف')
    content = models.TextField(verbose_name='التعليق')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    is_approved = models.BooleanField(default=True, verbose_name='موافق عليه')
    
    class Meta:
        verbose_name = 'تعليق'
        verbose_name_plural = 'التعليقات'
        ordering = ['created_at']
    
    def __str__(self):
        return f'تعليق بواسطة {self.author.username} على {self.post.title}'
