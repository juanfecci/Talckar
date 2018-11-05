from django import forms

class AssetForm(forms.Form):  
    address = forms.CharField(widget=forms.Textarea)

    