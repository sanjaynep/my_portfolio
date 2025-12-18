from myapp.models import message
from django import forms

class MessageForm(forms.ModelForm):
    class Meta:
        model = message
        fields = ['name', 'email', 'message']