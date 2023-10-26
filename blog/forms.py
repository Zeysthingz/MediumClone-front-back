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

    # automatically initialized widget
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['title'].widget.attrs.update({'class': 'form-control'})
