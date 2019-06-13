from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

class UpdateProfile(forms.ModelForm):
    nombre = forms.CharField(required=True)
    correo = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    profesion = forms.CharField(required=True)
    interes = forms.CharField(required=True)
    celular = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('nombre', 'correo', 'password', 'profesion', 'interes', 'celular')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('correo')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.correo = self.cleaned_data['correo']

        if commit:
            user.save()

        return user