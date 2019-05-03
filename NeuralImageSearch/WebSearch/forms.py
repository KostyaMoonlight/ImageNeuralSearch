from django import forms
 
class UserForm(forms.Form):
    info = forms.CharField(label="Add info:")
    image = forms.ImageField()