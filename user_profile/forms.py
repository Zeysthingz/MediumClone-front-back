from django import forms
from .models import Profile


class ProfileModelForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            'avatar',
            'instagram',
            'info',
        ]
