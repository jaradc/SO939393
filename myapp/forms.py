from django import forms
from .models import ModelTwo

class ModelTwoForm(forms.ModelForm):
    class Meta:
        model = ModelTwo
        fields = ['name', 'model_one', 'upload_file']
