from django import forms
from django.forms import fields
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['id','name','email','roll','address']
        widgets={

            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['id','name','email','roll','address']
        widgets={

            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }




        
class SingUp_form(UserCreationForm):
    password1=forms.CharField (label='Password',widget=forms.PasswordInput)
    password2=forms.CharField (label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']



# class BloodForm(forms.ModelForm):
#     class Meta:
#         model: Blood
#         fields= '__all__'

        