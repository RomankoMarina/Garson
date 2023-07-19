from django import forms
from geo.models import Region

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

