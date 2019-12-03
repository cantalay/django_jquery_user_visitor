from django import forms
from django.contrib.auth import models
from visitor import models


class VisitorForm(forms.ModelForm):
    class Meta:
        model = models.VisitorModel
        fields = ("name", "email", "title")
