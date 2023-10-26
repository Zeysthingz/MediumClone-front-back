from django import forms
from .models import Blog


class BlogModelForm(forms.ModelForm):
    tag = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Blog
        fields = [
            'title',
            'image',
            'content',
            'category',
            'tag',
        ]
