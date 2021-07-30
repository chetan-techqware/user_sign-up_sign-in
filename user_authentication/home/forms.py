from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib import messages


# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]
        #Model Meta is basically used to change the behavior of your model fields like changing order options,
        # verbose_name and lot of other options. 
        # It’s completely optional to add Meta class in your model.

        
    def clean_email(self):
        # Get the email
        email = self.cleaned_data['email']

        if User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = ("A user is already registered with the specified E-Mail address.")
            self.add_error('email', msg)
        
        elif User.DoesNotExist:
            return email



class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = ("There is no user registered with the specified E-Mail address.")
            self.add_error('email', msg)
        return email


# phone = forms.CharField(max_length=12, required=True)