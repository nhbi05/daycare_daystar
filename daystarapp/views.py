from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
#def index(request):
    #return render (request, 'daystarapp/index.html')
def landing_page (request):
    return render (request, 'daystarapp/landingpage.html')

#Register the user
def register(request):
    form3 = CreateUserForm()
    if request.method =="POST":
        form3 = CreateUserForm(request.POST)
        if form3.is_valid():
            form3.save()
            return redirect('login')
    context = {'form3':form3}
    return render(request, 'daystarapp/register.html',context=context)        

#- login a user
def login(request):
    form4 = LoginForm()
    if request.method =="POST":
        form4 = LoginForm(request, data=request.POST) 
        if form4.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
    return render(request, 'daystarapp/login.html', {
        'form4':form4,

        })     

def user_logout(request):
    auth.logout(request)
    return redirect('login')

         

@login_required(login_url='login')
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


def baby(request):
    return render (request, 'daystarapp/baby.html' , {
        'babies':Baby.objects.all()
    })

def sitter(request):
    return render(request, 'daystarapp/sitter.html', {
        'sitters':Sitter.objects.all()
        })
def procurement(request):
    return render(request, 'daystarapp/sitter.html', {
        'item':Procurement.objects.all()
        })

def payment(request):
    return render(request, 'daystarapp/sitter.html', {
        'payments':Payment.objects.all()
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
    
def view_baby(request, id):
    baby = Baby.objects.get(pk=id)
    return HttpResponseRedirect(reverse('baby'))


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
    Baby.objects.filter(id=id).delete()
    redirect_url = reverse('baby')
    return HttpResponseRedirect(redirect_url)

@login_required
#sitter views
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

            new_baby = Sitter(
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
            new_baby.save()
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

def view_sitter(request, id):
    sitter = Sitter.objects.get(id=id)
    return HttpResponseRedirect(reverse('sitter'))

def delete_sitter(request, id):
    Sitter.objects.filter(id=id).delete()
    redirect_url = reverse('sitter')
    return HttpResponseRedirect(redirect_url)

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
def create_payment(request, baby_id, payment_type):
    baby = Baby.objects.get(id=baby_id)
    payment = Payment(payment_no=baby, payment_type=payment_type, b_firstname=baby.first_name, b_lastname=baby.last_name)

    if payment_type == 'halfday':
        payment.amount = 10000
    elif payment_type == 'fullday':
        payment.amount = 15000
    elif payment_type == 'monthly':
        if payment_type == 'fullday':
            payment.amount = 15000 * 30
        else:
            payment.amount = 10000 * 30

    payment.save()

    # Redirect or render a template based on your needs
    return render(request, 'payment_created.html', {'payment': payment})