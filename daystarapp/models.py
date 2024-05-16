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
    b_DOB = models.DateTimeField()
    b_location = models.CharField(max_length=100)
    b_fathers_name = models.CharField(max_length=100)
    b_mothers_name = models.CharField(max_length=100)
    

    def __str__(self):
        return f'Baby:{self.b_firstname}{self.b_lastname}'
    
class BabyCheckin(models.Model):
    baby_name = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
    broughtby = models.CharField(max_length=100)
    timeIn = models.DateTimeField()    

class BabyCheckout(models.Model):
    PERIOD_OF_STAYS = (
        ('HALF_DAY', 'HALF_DAY'),
        ('FULL_DAY', 'FULL_DAY'),
    )
    baby_name = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
    picked_by = models.CharField(max_length=100)
    timeOut = models.DateTimeField() 
    period_of_stay = models.CharField(max_length=100, choices=PERIOD_OF_STAYS) 
    comment = models.CharField(max_length=100 , null=True, blank=True)  



class Sitter_id(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


    
class Sitter(models.Model):
    RELIGION = (
        ('ISLAM', 'ISLAM'),
        ('CHRISTIANITY', 'CHRISTIANITY'),
    )
    S_GENDERS = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    sitter_no = models.ForeignKey(Sitter_id, on_delete=models.CASCADE, null=True, blank=True)
    s_firstname = models.CharField(max_length=100)
    s_lastname = models.CharField(max_length=100)
    s_gender = models.CharField(max_length=100, choices= S_GENDERS )
    s_age = models.PositiveIntegerField()
    s_location = models.CharField(max_length=100, default="Kabalagala")
    s_nextofkin = models.CharField(max_length=100)
    s_NIN = models.CharField(max_length=100)
    s_recommendersname= models.CharField(max_length=100)
    s_educationlevel = models.CharField(max_length=100)
    s_contact = models.CharField(max_length=100)
    s_religion = models.CharField(max_length=100, choices=RELIGION)

    def __str__(self):
        return f'Sitter {self.s_firstname}{self.s_lastname}'    
   
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
    #receipt_no = models.CharField(max_length=100, null=True, blank=True)
    payment_mode = models.CharField(max_length=100 , choices= PAYMENT_MODES ,null=True, blank=True)
    payment_type = models.CharField (max_length=10, choices=PAYMENT_TYPES ,null=True, blank=True)
    payment_currency = models.CharField(max_length=10, choices=PAYMENT_CURRENCYS,null=True, blank=True)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.FloatField()

    def __str__(self):
        return f'Payment for {self.payment_name.b_firstname} {self.payment_name.b_lastname} - {self.payment_type} on {self.payment_date}'
    
class SitterPayment(models.Model):
    sitter_name = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    babies_assigned = models.ManyToManyField(Baby)
    status = models.BooleanField(max_length=100)
    paid_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Payment for {self.sitter_name}  on {self.paid_on}'
    


    
class Procurement(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    procurement_date = models.DateField(auto_now_add=True)
    procurement_cost = models.FloatField()

    def __str__(self):
        return f'Procurement of {self.item_name} on {self.procurement_date}'
     



class Doll(models.Model):
    doll_name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.doll_name


class Transaction(models.Model):
    buyer = models.ForeignKey('Baby', on_delete=models.CASCADE)
    doll = models.ForeignKey('Doll', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Default value set to 0
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate total amount based on doll price and quantity
        self.total_amount = self.doll.price * self.quantity
        super().save(*args, **kwargs)
        
        # Reduce doll quantity after transaction
        self.doll.quantity -= self.quantity
        self.doll.save()

    def __str__(self):
        return f"Transaction {self.id}: {self.buyer} bought {self.quantity} {self.doll}"

