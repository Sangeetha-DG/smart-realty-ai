from django import forms
from .models import HouseImage

class HouseImageForm(forms.ModelForm):
    class Meta:
        model = HouseImage
        fields = ['image']
