from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#set up signup form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text="A valid email address is required.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

#login form