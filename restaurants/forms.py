from django import forms
from .models import Restaurant, Item
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
		widgets = {
		"password": forms.PasswordInput()
		}

class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ['name', 'description', 'image', 'publish_date']
		
		widgets = {
			"publish_date": forms.DateInput(attrs={"type":"date"})
		}



class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['name', 'description', 'price']
		
	