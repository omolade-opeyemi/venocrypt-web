from django import forms

class encryptForm(forms.Form):
    password = forms.CharField(max_length=100)
    text  = forms.CharField(widget=forms.Textarea)