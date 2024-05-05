from django.db import models
from django.utils import timezone

# Create your models here.
class Baby_id(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Baby(models.Model):
    baby_id = models.ForeignKey(Baby_id, on_delete=models.CASCADE, null=True, blank=True)
    b_firstname = models.CharField(max_length=100)
    b_lastname = models.CharField(max_length=100)
    b_gender = models.CharField(max_length=100)
    b_age = models.PositiveIntegerField()
    b_location = models.CharField(max_length=100)
    b_parentsname = models.CharField(max_length=100)
    b_broughtby = models.CharField(max_length=100)
    b_pickedby = models.CharField(max_length=100)
    periodofstay= models.CharField(max_length=100)
    timein = models.DateTimeField(auto_now_add=True)
    timeout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Baby:{self.b_firstname}{self.b_lastname}'

class Sitter_id(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


    
class Sitter(models.Model):
    sitter_no = models.ForeignKey(Sitter_id, on_delete=models.CASCADE, null=True, blank=True)
    s_firstname = models.CharField(max_length=100)
    s_lastname = models.CharField(max_length=100)
    s_gender = models.CharField(max_length=100)
    s_age = models.PositiveIntegerField()
    s_location = models.CharField(max_length=100, default="Kabalagala")
    s_nextofkin = models.CharField(max_length=100)
    s_NIN = models.CharField(max_length=100)
    s_recommendersname= models.CharField(max_length=100)
    s_educationlevel = models.CharField(max_length=100)
    s_contact = models.CharField(max_length=100)

    def __str__(self):
        return f'Baby:{self.s_firstname}{self.s_lastname}'    
    
class Payment(models.Model):
    payment_name = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
    PAYMENT_TYPES = (
        ('halfday', 'Half Day'),
        ('fullday', 'Full Day'),
    )
    PAYMENT_MODES = (
        ('daily', 'Daily'),
        ('monthly', 'Monthly'),
    )

    PAYMENT_CURRENCYS = (
        ('USD', 'USD'),
        ('UGX', 'UGX'),
    )
    receipt_no = models.CharField(max_length=100, null=True, blank=True)
    payment_mode = models.CharField(max_length=100 , choices= PAYMENT_MODES, null=True, blank=True)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPES)
    payment_currency = models.CharField(max_length=10, choices=PAYMENT_CURRENCYS, null=True , blank=True)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.FloatField()

    def __str__(self):
        return f'Payment for {self.payment_name.b_firstname} {self.payment_name.b_lastname} - {self.payment_type} on {self.payment_date}'
    
#class SitterPayment(models.Model):

    
class Procurement(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    procurement_date = models.DateField(auto_now_add=True)
    procurement_cost = models.FloatField()

    def __str__(self):
        return f'Procurement of {self.item_name} on {self.procurement_date}'
     


    