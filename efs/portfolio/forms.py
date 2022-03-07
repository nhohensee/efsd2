from django import forms
from .models import Customer, Stock, Investment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)

	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		if commit:
			user.save()
		return user

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)

class StockForm(forms.ModelForm):
   class Meta:
       model = Stock
       fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)

class InvestmentForm(forms.ModelForm):
   class Meta:
       model = Investment
       fields = ('customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
       'recent_date',)

