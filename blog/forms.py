from django import forms
from .models import Blog
from tinymce.widgets import TinyMCE
from django.core.validators import MinLengthValidator


class BlogModelForm(forms.ModelForm):
    tag = forms.CharField(max_length=200, required=False)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 20, 'rows': 10}))
    title = forms.CharField(validators=[MinLengthValidator(3, message="Title must be at least 3 characters.")])

    class Meta:
        model = Blog
        fields = [
            'title',
            'image',
            'content',
            'category',
            'tag',
        ]

    # automatically initialized widget
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['title'].widget.attrs.update({'class': 'form-control'})
