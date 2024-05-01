from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter e-mail'}))
    password1 = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter name'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
