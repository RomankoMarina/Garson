from django import forms
from geo.models import Street


class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = '__all__'

