from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False,max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=1000)