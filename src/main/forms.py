from django import forms
from .models import ClassImage


class ImageForm(forms.ModelForm):
    class Meta:
        model = ClassImage
        fields = ['upload_image', ]
