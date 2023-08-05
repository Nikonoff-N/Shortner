from django import forms
from django.forms import ModelForm
from .models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ("url",)
        widgets = {
            "url": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "https://ya.ru"}
            )
        }
