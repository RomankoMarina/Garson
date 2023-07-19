from django import forms
from menu.models import Feature


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = '__all__'
