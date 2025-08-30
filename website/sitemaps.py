
# إضافة sitemap.xml
# website/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import BlogPost

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['website:home', 'website:about', 'website:services', 
                'website:portfolio', 'website:contact', 'blog:blog_list']

    def location(self, item):
        return reverse(item)

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at
