from django import forms


def title_check(value):
    if len(value) < 3:
        raise forms.ValidationError("Title must be at least 3 characters Our own validator.")
