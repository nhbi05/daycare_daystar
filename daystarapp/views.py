from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def landing_page (request):
    return render (request, 'daystarapp/landingpage.html')

#Register the user
#def register(request):
    form3 = CreateUserForm()
    if request.method == "POST":
        form3 = CreateUserForm(request.POST)
        if form3.is_valid():
            form3.save()
            return redirect('login')
    context = {'form3': form3}
    return render(request, 'daystarapp/register.html', context=context)        



def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Optionally, you can log in the user after registration
            # login(request, user)
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CreateUserForm()
    return render(request, 'daystarapp/register.html', {'form3': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('index')
            else:
                # Return an 'invalid login' error message.
                # You might want to handle this in a different way, like displaying an error message in the form.
                return render(request, 'daystarapp/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'daystarapp/login.html', {'form': form})


def user_logout(request):
    auth.logout(request)
    return redirect('login')

         

@login_required()
def index(request):
    # stats
    count_babies = Baby.objects.count()
    count_sitters = Sitter.objects.count()
    count_payments = Payment.objects.count()
    context = {
        "count_babies": count_babies,
        "count_sitters": count_sitters,
        "count_payments": count_payments,
    }
    return render(request, "daystarapp/index.html", context)



@login_required
#baby views
def baby(request):
    return render (request, 'daystarapp/baby.html' , {
        'babies':Baby.objects.all()
    })

@login_required
def addBaby(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['b_firstname']
            new_last_name = form.cleaned_data['b_lastname']
            new_gender = form.cleaned_data['b_gender']
            new_age = form.cleaned_data['b_age']
            new_parentsname = form.cleaned_data['b_parentsname']
            new_pickedby = form.cleaned_data['b_pickedby']
            new_broughtby = form.cleaned_data['b_broughtby']
            new_periodofstay = form.cleaned_data['periodofstay']
            new_location = form.cleaned_data['b_location']

            new_baby = Baby(
                b_firstname = new_first_name,
                b_lastname = new_last_name,
                b_gender = new_gender,
                b_age = new_age,
                b_location = new_location,
                b_pickedby = new_pickedby,
                b_broughtby = new_broughtby,
                periodofstay = new_periodofstay,
                b_parentsname = new_parentsname,
            )
            new_baby.save()
            return render(request, 'daystarapp/baby_reg.html', {
                'form': BabyForm(),
                'success': True,
            })
        else:
            print ("Form is not valid")
            return render(request, 'daystarapp/baby_reg.html', {
              'form': BabyForm(),
               'success': False,
            })
    else:
        form = BabyForm()
        return render(request, 'daystarapp/baby_reg.html', {
            'form' : BabyForm()
        })    
@login_required   
def view_baby(request, id):
    baby = Baby.objects.get(pk=id)
    return HttpResponseRedirect(reverse('baby'))

@login_required
def babyedit(request, id):
    baby = Baby.objects.get(id=id)
    if request.method == 'POST':
        form2 = BabyForm(request.POST, instance=baby)
        if form2.is_valid():
            form2.save()
            return redirect('baby')
        else:
            print ("Form is not valid")
    else:
        form2 = BabyForm(instance=baby)
    return render(request, 'daystarapp/b_edit.html', {
        "form2":form2,
        'baby': baby
    }) 
@login_required
def delete_baby(request, id):
    baby = Baby.objects.get(id=id)

    if request.method == 'POST':
        baby.delete()
        redirect_url = reverse('baby')
        return HttpResponseRedirect(redirect_url)
    else:
        return render(request, 'daystarapp/baby_delete.html', {'baby': baby})

@login_required
#sitter views
def sitter(request):
    return render(request, 'daystarapp/sitter.html', {
        'sitters':Sitter.objects.all()
        })

@login_required
def addSitter(request):
    if request.method == 'POST':
        form1 = SitterForm(request.POST)
        if form1.is_valid():
            new_first_name = form1.cleaned_data['s_firstname']
            new_last_name = form1.cleaned_data['s_lastname']
            new_gender = form1.cleaned_data['s_gender']
            new_age = form1.cleaned_data['s_age']
            new_recommendersname = form1.cleaned_data['s_recommendersname']
            new_contact = form1.cleaned_data['s_contact']
            new_NIN = form1.cleaned_data['s_NIN']
            new_educationlevel = form1.cleaned_data['s_educationlevel']
            new_location = form1.cleaned_data['s_location']
            new_nextofkin = form1.cleaned_data['s_nextofkin']

            new_sitter = Sitter(
                s_firstname = new_first_name,
                s_lastname = new_last_name,
                s_gender = new_gender,
                s_age = new_age,
                s_location = new_location,
                s_nextofkin = new_nextofkin,
                s_recommendersname = new_recommendersname,
                s_educationlevel = new_educationlevel,
                s_NIN = new_NIN,
                s_contact = new_contact,
            )
            new_sitter.save()
            return render(request, 'daystarapp/sitter_reg.html', {
                'form1': SitterForm(),
                'success': True,
            })
        else:
            print ("Form is not valid")
            return render(request, 'daystarapp/sitter_reg.html', {
              'form1': SitterForm(),
               'success': False,
            })
    else:
        form1= SitterForm()
        return render(request, 'daystarapp/sitter_reg.html', {
            'form1' : SitterForm()
        }) 
@login_required
def view_sitter(request, id):
    sitter = Sitter.objects.get(id=id)
    return HttpResponseRedirect(reverse('sitter'))

def delete_sitter(request, id):
    sitter = Sitter.objects.get(id=id)
    if request.method == 'POST':
        sitter.delete()
        return redirect('sitter')
    return render(request, 'daystarapp/sitter_delete.html', {'sitter': sitter})

@login_required
def sitter_edit(request, id):
    sitter = Sitter.objects.get(id=id)
    if request.method == 'POST':
        form1 = SitterForm(request.POST, instance=sitter)
        if form1.is_valid():

            form1.save()
            return redirect('sitter')
        else:
            print ("Form is not valid")
    else:
        form1 = SitterForm(instance=sitter)
    return render(request, 'daystarapp/s_edit.html', {
        "form1":form1,
        'sitter': sitter
    }) 





#Payment views
@login_required
def payment(request):
    return render(request, 'daystarapp/payments.html', {
        'payments':Payment.objects.all()
        })
@login_required
def view_payment(request, id):
    payment = Payment.objects.get(id=id)
    return HttpResponseRedirect(reverse('payments'))

@login_required
def create_payment(request):
    if request.method == 'POST':
        form5 = PaymentForm(request.POST)
        if form5.is_valid():
            new_payment_name = form5.cleaned_data['payment_name']
            new_payment_type = form5.cleaned_data['payment_type']
            new_payment_mode = form5.cleaned_data['payment_mode']
            new_payment_currency = form5.cleaned_data['payment_currency']
            new_amount = form5.cleaned_data['amount']

            new_payment = Payment(
                payment_name = new_payment_name,
                payment_type = new_payment_type,
                payment_mode = new_payment_mode,
                payment_currency = new_payment_currency,
                amount = new_amount,)
            new_payment.save()
            return render(request, 'daystarapp/payment_reg.html', {
                'form5': PaymentForm(),
                'success': True,
            })
        else:
            print ("Form is not valid")
            return render(request, 'daystarapp/payment_reg.html', {
              'form5': PaymentForm(),
               'success': False,
            })
    else:
        form5= PaymentForm()
        return render(request, 'daystarapp/payment_reg.html', {
            'form5' : PaymentForm()
        }) 

@login_required
def payment_update(request, id):
    payment = Payment.objects.get(id=id)
    if request.method == 'POST':
        form5 = PaymentForm(request.POST, instance=payment)
        if form5.is_valid():
            form5.save()
            return redirect('payments', id=id)
    else:
        form5 = PaymentForm(instance=payment)
    return render(request, 'daystarapp/payment_reg.html', {'form5': form5})

@login_required
def payment_delete(request, id):
    payment = Payment.objects.get(id=id)
    if request.method == 'POST':
        payment.delete()
        return redirect('payments')
    return render(request, 'daystarapp/payment_delete.html', {'payment': payment})





#siter payments
@login_required
# Read operation
def sitter_payment(request):
    payment_sitter= SitterPayment.objects.all()
    for payment in payment_sitter :
        payment.payment_amount = payment.babies_assigned.all().count() * 3000
    return render(request, 'daystarapp/sitter_status.html', {
           'payment_sitter' : payment_sitter})

#def view_payment(request, id):
    #sitter_payment = Payment.objects.get(id=id)
    #return HttpResponseRedirect(reverse('payments'))

@login_required
# Update operation
def update_sitter_payment(request, id):
    sitter_payment = SitterPayment.objects.get(id=id)
    if request.method == 'POST':
        form7 = SitterPaymentForm(request.POST, instance=sitter_payment)
        if form7.is_valid():
            form7.save()
            return render(request, 'daystarapp/edit.html', {
                'form7': form7,
                'success': True,
            })
    else:
        form = SitterPaymentForm(instance=sitter_payment)
    return render(request, 'daystarapp/edit.html', {
        'form7': form7,
        'success': False,
    })
@login_required
# Delete operation
def delete_sitter_payment(request, id):
    sitter_payment = SitterPayment.objects.get( id=id)
    sitter_payment.delete()
    return redirect('sitter_payment_list')  # Redirect to the list view after deletion

@login_required
def addSitter_status(request):
    if request.method == 'POST':
        form7 = SitterPaymentForm(request.POST)

        if form7.is_valid():
            new_sitter_name = form7.cleaned_data['sitter_name']
            new_babies_assigned = form7.cleaned_data['babies_assigned']
            new_status = form7.cleaned_data['status']

            new_sitter_payment = SitterPayment(
                sitter_name=new_sitter_name,
                status=new_status,
            )
            new_sitter_payment.save()
            new_sitter_payment.babies_assigned.set(new_babies_assigned)  # Assign babies using set()
            return render(request, 'daystarapp/s_paymentadd.html', {
                'form7': SitterPaymentForm(),
                'success': True,
            })
        else:
            print("Form is not valid")
            return render(request, 'daystarapp/s_paymentadd.html', {
                'form7': SitterPaymentForm(),
                'success': False,
            })
    else:
        form7 = SitterPaymentForm()

    return render(request, 'daystarapp/s_paymentadd.html', {
        'form7': form7,  # Use the form instance instead of creating a new one
    })




#procurement views
@login_required
def procurement_landingpage(request):
    return render(request, 'daystarapp/procurementhome.html')

@login_required
def procurement(request):
    return render(request, 'daystarapp/procurement.html', {
        'procurement_items':Procurement.objects.all()
        })
@login_required
def view_procurement(request, id):
    new_procurement = Procurement.objects.get(id=id)
    return HttpResponseRedirect(reverse('procurementhome'))
@login_required
def create_procurement(request):
    if request.method == 'POST':
        form8 = ProcurementForm(request.POST)
        if form8.is_valid():
            new_item_name = form8.cleaned_data['item_name']
            new_quantity = form8.cleaned_data['quantity']
            new_procurement_cost = form8.cleaned_data['procurement_cost']

            new_procurement = Procurement(
                item_name = new_item_name,
                quantity = new_quantity,
                procurement_cost= new_procurement_cost,
                    )
            new_procurement.save()
            return render(request, 'daystarapp/procurement_reg.html', {
                'form8': ProcurementForm(),
                'success': True,
            })
        else:
            print ("Form is not valid")
            return render(request, 'daystarapp/procurement_reg.html', {
              'form8': ProcurementForm(),
               'success': False,
            })
    else:
        form8= ProcurementForm()
        return render(request, 'daystarapp/procurement_reg.html', {
            'form8' : ProcurementForm()
        }) 

@login_required
def procurement_update(request, id):
    item = Procurement.objects.get(id=id)
    if request.method == 'POST':
        form8 = ProcurementForm(request.POST, instance=item)
        if form8.is_valid():
            form8.save()
            return render(request, 'daystarapp/procurement_edit.html', {
                'form8': form8,
                'success': True,
            })
    else:
        form8 = ProcurementForm(instance=item)
    return render(request, 'daystarapp/procurement_edit.html', {
        'form8': form8,
        'success': False,
    })

@login_required
def procurement_delete(request, id):
    item = Procurement.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('procurement')
    return render(request, 'daystarapp/confirm_delete.html', {'item': item})




#dolls views
@login_required
def all_dolls(request):
    dolls = Doll.objects.all()
    return render(request, 'daystarapp/dolls.html', {'dolls': dolls})

@login_required
def create_doll(request):
    if request.method == 'POST':
        form9 = DollForm(request.POST)
        if form9.is_valid():
            new_doll_name = form9.cleaned_data['doll_name']
            new_quantity = form9.cleaned_data['quantity']
            new_price = form9.cleaned_data['price']

            new_doll = Doll(
                doll_name = new_doll_name,
                quantity = new_quantity,
                price= new_price,
                    )
            new_doll.save()
            return render(request, 'daystarapp/doll_reg.html', {
                'form9': DollForm(),
                'success': True,
            })
        else:
            print ("Form is not valid")
            return render(request, 'daystarapp/doll_reg.html', {
              'form9': DollForm(),
               'success': False,
            })
    else:
        form9= DollForm()
        return render(request, 'daystarapp/doll_reg.html', {
            'form9' : DollForm()
        }) 
    
@login_required
def view_doll(request,id):
    doll = Doll.objects.get(id=id)
    return render(request, 'view_doll.html', {'doll': doll})


@login_required
def update_doll(request, id):
    doll = Doll.objects.get(id=id)
    if request.method == 'POST':
        form_doll = DollForm(request.POST, instance=doll)
        if form_doll.is_valid():
            form_doll.save()
            return redirect('dolls')  # Redirect to view doll page after successful update
    else:
        form_doll = DollForm(instance=doll)
    return render(request, 'daystarapp/doll_update.html', {
        'form_doll': form_doll,
        'doll': doll,
    })

@login_required
def delete_doll(request, id):
    doll = Doll.objects.get(id=id)
    if request.method == 'POST':
        doll.delete()
        return redirect('dolls')
    return render(request, 'daystarapp/doll_delete.html', {'doll': doll})


#Doll Transaction

def make_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            return redirect('transaction_list')
        else:
            print("form is invalid")
    else:
        form = TransactionForm()
    return render(request, 'daystarapp/make_transaction.html', {'form': form})





def transaction_detail(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    return render(request, 'daystarapp/transaction_detail.html', {'transaction': transaction})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'daystarapp/transaction_list.html', {'transactions': transactions})


def receipt(request, transaction_id):
    transaction = Transaction.objects.get(pk=transaction_id)
    return render(request, 'receipt.html', {'transaction': transaction})


def transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'daystarapp/transactions.html', {'transactions': transactions})





