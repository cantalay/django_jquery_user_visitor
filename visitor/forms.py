from django import forms
from visitor import models

class VisitorForm(forms.ModelForm):
    class Meta:
        model = models.VisitorModel
        fields = ("name","email","title")