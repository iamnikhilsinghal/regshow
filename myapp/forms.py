from django import forms
from django.contrib.auth.models import User
from .models import *
class userform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your name'}),required=True,max_length=30)
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}),required=True,max_length=30)
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First name'}),required=True,max_length=30)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last name'}),required=True,max_length=30)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}),required=True,max_length=30)
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password again'}),required=True,max_length=30)
    class Meta():			#create instance in another class
        model=User			#created model of User class
        fields=['username','email','first_name','last_name','password','confirm_password']
    def clean_confirm_password(self):
        p = self.cleaned_data['password']
        cp = self.cleaned_data['confirm_password']
        if (p != cp):
            raise forms.ValidationError("Confirm Password and Password Must be Same")
        else:
            if (len(p) < 8):
                raise forms.ValidationError("Password must contains atleast 8 Character")
            if (p.isdigit()):
                raise forms.ValidationError("Password must contains aleast a character")
class studentform(forms.ModelForm):
	class Meta():
		model=Student
		fields='__all__'