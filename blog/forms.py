
# blog/forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'excerpt', 'image', 'is_published']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'excerpt',
            'content',
            'image',
            'is_published',
            Submit('submit', 'حفظ المقالة', css_class='btn btn-primary')
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'اكتب تعليقك هنا...'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'content',
            Submit('submit', 'إضافة تعليق', css_class='btn btn-primary')
        )
