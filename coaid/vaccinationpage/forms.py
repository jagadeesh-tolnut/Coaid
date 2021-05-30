from django import forms
from .models import Search_by_pin

class SearchByPinForm(forms.ModelForm):
    class Meta:
        model = Search_by_pin
        fields = '__all__'