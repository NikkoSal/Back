from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
