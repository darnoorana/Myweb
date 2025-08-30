from django.shortcuts import render

# Create your views here.
# website/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import WebsiteRequest, ContactMessage, JobApplication
from .forms import WebsiteRequestForm, ContactForm, JobApplicationForm

def home(request):
    """الصفحة الرئيسية"""
    return render(request, 'website/home.html')

def about(request):
    """صفحة من نحن"""
    return render(request, 'website/about.html')

def services(request):
    """صفحة الخدمات"""
    return render(request, 'website/services.html')

def portfolio(request):
    """صفحة أعمالنا"""
    return render(request, 'website/portfolio.html')

def charity_projects(request):
    """صفحة المشاريع الخيرية"""
    return render(request, 'website/charity_projects.html')

def join_us(request):
    """صفحة انضم لنا"""
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إرسال طلب التوظيف بنجاح! سنتواصل معك قريباً.')
            return redirect('website:join_us')
    else:
        form = JobApplicationForm()
    
    return render(request, 'website/join_us.html', {'form': form})

def request_website(request):
    """صفحة طلب موقع"""
    if request.method == 'POST':
        form = WebsiteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إرسال طلبك بنجاح! سنتواصل معك خلال 24 ساعة.')
            return redirect('website:request_website')
    else:
        form = WebsiteRequestForm()
    
    return render(request, 'website/request_website.html', {'form': form})

def contact(request):
    """صفحة التواصل"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إرسال رسالتك بنجاح! سنرد عليك قريباً.')
            return redirect('website:contact')
    else:
        form = ContactForm()
    
    return render(request, 'website/contact.html', {'form': form})
