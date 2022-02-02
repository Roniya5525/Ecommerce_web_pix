from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	firstname = forms.CharField(max_length=50)
	lastname = forms.CharField(max_length=50)

	class Meta:
		model = User
		fields = ['username','firstname','lastname', 'email', 'password1', 'password2']