from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget

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
        fields = [ 'b_firstname', 'b_lastname','b_age','b_gender','b_fathers_name','b_location','b_mothers_name','b_DOB']
        labels = { 
            'b_firstname': 'First Name', 
            'b_lastname': 'Last Name',
            'b_age': 'Age',
            'b_gender':'Gender',
            'b_fathers_name':'Fathers Name',
            'b_mothers_name':'Moms Name',
            'b_location': 'Location',
            'b_DOB': 'Date of Birth',
            }
    widgets = {
        'b_firstname':forms.TextInput(attrs={'placeholder': 'Name'}), 
        'b_lastname':forms.TextInput(attrs={'class':'form-control'}), 
        'b_age':forms.NumberInput(attrs={'class':'form-control'}), 
        'b_gender':forms.TextInput(attrs={'class':'form-control'}), 
        'b_fathers_name':forms.TextInput(attrs={'class':'form-control'}), 
        'b_mothers_name':forms.TextInput(attrs={'class':'form-control'}), 
        'b_location':forms.TextInput(attrs={'class':'form-control'}), 
        'b_DOB' :forms.DateField(widget=forms.DateInput(attrs={'type':'date','placeholder': 'Search'}))

    }


class BabyCheckinForm(forms.ModelForm):
    class Meta:
        model = BabyCheckin
        fields = [ 'baby_name', 'broughtby','timeIn']
        labels = { 
            'baby_name': 'Baby Name', 
            'broughtby': 'Brought By',
            'timeIn': 'Time In',
            
            }
    widgets = {
        'baby_name':forms.Select(attrs={'class':'form-control'}), 
        'broughtby':forms.TextInput(attrs={'class':'form-control'}), 
        'timeIn' :forms.DateField(widget=forms.DateInput(attrs={'type':'date','placeholder': 'Search'}))
        
    }

class BabyCheckoutForm(forms.ModelForm):
    class Meta:
        model = BabyCheckout
        fields = [ 'baby_name', 'picked_by','timeOut','period_of_stay','comment']
        labels = { 
            'baby_name': 'Baby Name', 
            'picked_by': 'Picked By',
            'period_of_stay':'Period of Stay',
            'timeOut': 'Time Out',
            'comment' : 'comment'
            }
    widgets = {
        'baby_name':forms.Select(attrs={'class':'form-control'}), 
        'picked_by':forms.TextInput(attrs={'class':'form-control'}), 
        'comment':forms.TextInput(attrs={'class':'form-control'}), 
        'period_of_stay':forms.Select(attrs={'class':'form-control'}), 
        'timeOut' :forms.DateField(widget=forms.DateInput(attrs={'type':'date','placeholder': 'Search'}))
        
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

class PaymentForm(forms.ModelForm):
    class Meta: 
        model = Payment
        fields = [ #'receipt_no',
                  'payment_name','payment_type', 'payment_mode','payment_currency', 'amount'] 
        labels = {
        #'receipt_no': 'Receipt No',   
        'payment_name' :'Payment Name',   
        'payment_type' :'Payment type', 
        'payment_mode': 'Payment Mode',
        'payment_currency': 'Payment Currency',
        'amount':'Amount',
          }  
    widgets = {
        #'receipt_no':forms.Select(attrs={'class':'form-control'}),
        'payment_name':forms.Select(attrs={'class':'form-control'}),
        'payment_type':forms.Select(attrs={'class':'form-control'}),
        'payment_mode':forms.Select(attrs={'class':'form-control'}), 
        'payment_currency':forms.Select(attrs={'class':'form-control'}), 
        'amount': forms.Select(attrs={'class':'form-control'}),
        
    } 

class SitterPaymentForm(forms.ModelForm):
    class Meta: 
        model = SitterPayment
        fields = [ #'receipt_no',
                  'sitter_name','babies_assigned', 'status'] 
        labels = {
        #'receipt_no': 'Receipt No',   
        'sitter_name ':'Sitter Name',   
        'babies_assigned' :'Babies Assigned', 
        'status': 'Status',
        #'daily_salary': 'Daily Salary',
          }  
    widgets = {
        #'receipt_no':forms.Select(attrs={'class':'form-control'}),
        'sitter_name':forms.Select(attrs={'class':'form-control'}),
        'babies_assigned': forms.SelectMultiple(attrs={'class': 'form-control'}),
        'status':forms.CheckboxInput(attrs={'class':'form-control'}), 
       # 'daily_salary': forms.NumberInput(attrs={'class':'form-control'})
        
    }  
    

class ProcurementForm(forms.ModelForm):
    class Meta: 
        model = Procurement
        fields = [ #'receipt_no',
                  'item_name', 'quantity','procurement_cost'] 
        labels = {
        #'receipt_no': 'Receipt No',   
        'item_name' :'Item_name',   
        'quantity' :'Quantity', 
        'procurement_cost': 'Procurement Cost',
          }  
    widgets = {
        #'receipt_no':forms.Select(attrs={'class':'form-control'}),
        'item_name':forms.TextInput(attrs={'class':'form-control'}),
        'quantity':forms.NumberInput(attrs={'class':'form-control'}),
        'procurement_cost':forms.NumberInput(attrs={'class':'form-control'}), 
    }     
   

class DollForm(forms.ModelForm):
    class Meta:
        model = Doll
        fields = ['doll_name', 'price', 'quantity']
        labels = {
            'doll_name': 'Doll Name',
            'price': 'Price',
            'quantity': 'Quantity'
        }
        widgets = {
            'doll_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['buyer', 'doll', 'quantity']
        labels = {
            'buyer': 'Buyer',
            'doll': 'Doll',
            'quantity': 'Quantity',
            
        }
        widgets = {
            'buyer': forms.Select(attrs={'class': 'form-select'}),
            'doll': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }

        
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)