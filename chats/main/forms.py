from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        exclude = ['password']
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # Exclude 'password' field from the form
        self.fields.pop('password', None)

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'placeholder': 'USERNAME'})
        self.fields['email'].widget.attrs.update({'placeholder': 'EMAIL'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'PASSWORD'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'CONFIRM PASSWORD'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']