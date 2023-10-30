from django import forms
from .models import Blog
from tinymce.widgets import TinyMCE


class BlogModelForm(forms.ModelForm):
    tag = forms.CharField(max_length=200, required=False)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 20, 'rows': 10}))

    class Meta:
        model = Blog
        fields = [
            'title',
            'image',
            'content',
            'category',
            'tag',
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError('Please enter valid title more than 2 characters')
        return title

    # automatically initialized widget
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['title'].widget.attrs.update({'class': 'form-control'})
