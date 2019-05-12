from django import forms
 
class UserForm(forms.Form):
    info = forms.CharField(label="Add info:")
    image = forms.ImageField()

class ProductForm(forms.Form):
    name = forms.CharField(label="Product name:")
    url = forms.CharField(label='URL:')
    image = forms.ImageField()