from django import forms
from place.models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'

