from django import forms
from .models import Plane


class AddForm(forms.ModelForm):

    class Meta:
        model = Plane
        fields = ['name', 'content']



