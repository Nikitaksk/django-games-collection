from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': 'Password', })
                                , help_text="Required. Your password can’t be too similar to your other personal "
                                            "information, be entirely numeric, too short or commonly used")

    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': 'Repeat your password',
    }), help_text="Enter the same password as before, for verification.")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'input', 'placeholder': 'Username'}
            ),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))
