from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Baby)
admin.site.register(Sitter)
admin.site.register(SitterPayment)
admin.site.register(Payment)
admin.site.register(Procurement)
admin.site.register(Doll)
admin.site.register(Transaction)