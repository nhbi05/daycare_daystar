from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

#register or create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

#Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())        

#




class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = [ 'b_firstname', 'b_lastname','b_age','b_gender','b_parentsname','b_broughtby','b_pickedby','periodofstay','b_location']
        labels = { 
            'b_firstname': 'First Name', 
            'b_lastname': 'Last Name',
            'b_age': 'Age',
            'b_gender':'Gender',
            'b_parentsname':'Parents Name',
            'b_broughtby': 'Brought by',
            'b_pickedby': 'Picked by',
            'periodofstay': 'Period of Stay',
            'b_location': 'Location',
            }
    widgets = {
        'b_firstname':forms.TextInput(attrs={'class':'form-control'}), 
        'b_lastname':forms.TextInput(attrs={'class':'form-control'}), 
        'b_age':forms.NumberInput(attrs={'class':'form-control'}), 
        'b_gender':forms.TextInput(attrs={'class':'form-control'}), 
        'b_parentsname':forms.TextInput(attrs={'class':'form-control'}), 
        'b_broughtby':forms.TextInput(attrs={'class':'form-control'}), 
        'b_pickedby':forms.TextInput(attrs={'class':'form-control'}), 
        'periodofstay':forms.TextInput(attrs={'class':'form-control'}),
        'b_location':forms.TextInput(attrs={'class':'form-control'}), 
        
    }

class SitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = [ 's_firstname', 's_lastname','s_age','s_gender','s_nextofkin','s_recommendersname','s_NIN','s_educationlevel','s_location','s_contact']
        labels = { 
            's_firstname': 'First Name', 
            's_lastname': 'Last Name',
            's_age': 'Age',
            's_gender':'Gender',
            's_recommendersname':'Recommenders Name',
            's_location': 'Location',
            's_contact': 'Contact',
            's_nextofkin': 'Next of Kin',
            's_NIN': 'NIN',
            's_educationlevel': 'Education level',
            }
    widgets = {
        's_firstname':forms.TextInput(attrs={'class':'form-control'}), 
        's_lastname':forms.TextInput(attrs={'class':'form-control'}), 
        's_age':forms.NumberInput(attrs={'class':'form-control'}), 
        's_gender':forms.TextInput(attrs={'class':'form-control'}), 
        's_recommendersname':forms.TextInput(attrs={'class':'form-control'}), 
        's_NIN':forms.TextInput(attrs={'class':'form-control'}), 
        's_educationlevel':forms.TextInput(attrs={'class':'form-control'}), 
        's_nextofkin':forms.TextInput(attrs={'class':'form-control'}),
        's_location':forms.TextInput(attrs={'class':'form-control'}), 
        's_contact':forms.TextInput(attrs={'class':'form-control'}), 
        
    }    

            