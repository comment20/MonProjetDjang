from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='prenom')
    last_name = forms.CharField(label='nom')
    email = forms.EmailField(label='Adress Email')
    password1 = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
        strip=False,
        )
    password2 = forms.CharField(
        label='répétez votre Mot de passe', 
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
        strip=False,
        )

    class Meta(UserCreationForm.Meta):
        
        fields =UserCreationForm.Meta.fields + ("first_name", "last_name", "email", "password1", "password2")
