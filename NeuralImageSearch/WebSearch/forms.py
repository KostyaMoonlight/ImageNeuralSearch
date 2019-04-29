from django import forms
 
class UserForm(forms.Form):
    name = forms.CharField(label="Enter your name:")
    age = forms.IntegerField(initial=123)
    image = forms.ImageField()