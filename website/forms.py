# website/forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from .models import WebsiteRequest, ContactMessage, JobApplication

class WebsiteRequestForm(forms.ModelForm):
    class Meta:
        model = WebsiteRequest
        fields = ['website_name', 'domain', 'client_name', 'email', 'phone', 
                 'whatsapp', 'telegram', 'description', 'additional_requirements']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'additional_requirements': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('website_name', css_class='form-group col-md-6 mb-3'),
                Column('domain', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('client_name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-3'),
                Column('whatsapp', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            'telegram',
            'description',
            'additional_requirements',
            Submit('submit', 'إرسال الطلب', css_class='btn btn-primary btn-lg w-100')
        )

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-3'),
                Column('subject', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            'message',
            Submit('submit', 'إرسال الرسالة', css_class='btn btn-primary btn-lg w-100')
        )

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'phone', 'position', 'experience_level', 
                 'skills', 'portfolio_url', 'cv_file', 'cover_letter']
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 3}),
            'cover_letter': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('phone', css_class='form-group col-md-4 mb-3'),
                Column('position', css_class='form-group col-md-4 mb-3'),
                Column('experience_level', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            'skills',
            Row(
                Column('portfolio_url', css_class='form-group col-md-6 mb-3'),
                Column('cv_file', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            'cover_letter',
            Submit('submit', 'تقديم الطلب', css_class='btn btn-primary btn-lg w-100')
        )
