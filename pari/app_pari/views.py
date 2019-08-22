from django.shortcuts import render,redirect
import datetime
from app_pari.api import Spot
from django.contrib.auth import authenticate , login ,logout
#from django.contrib.auth.forms import UserCreationForm #generateur de formulaire django
from django.contrib import messages #pour les messages de validation
# from app_pari.models import Users 

from django.contrib.auth.models import User
from django import forms
from django.template import RequestContext
import random


class Form_register(forms.Form):
    username= forms.CharField(label="username",max_length=100,required=True)
    first_name = forms.CharField(label="first_name",max_length=100,required=True)
    last_name = forms.CharField(label="last_name",max_length=100,required=True)
    email = forms.EmailField(label="email",max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput)

class Form_login(forms.Form):
    username= forms.CharField(label="username",max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput)

class Form_choice(forms.Form):
    ticket = forms.CharField(label="numero de ticket ici",max_length=5,required=True)
    


def handler404(request,exception):
    return render(request,'../errors/404.html',{},status=404)
def handler500(request):
    return render(request,'../errors/500.html',{},status=500)
    
    
 


def index(request):
    
    this_day = datetime.datetime.today().date()
    week_day = ['lundi','mardi','mercredi','jeudi','vendredi','samedi']
    return render(request,'app_pari/index.html',{'this_day': this_day,'week_day':week_day})

def sport(request):
    sports = Spot.all()
    return render(request,'app_pari/sport.html',{'sports': sports })

def details(request,id):
    #ligue = Ligue.found(id)
    sports = Spot.find(id)
    return render(request,'app_pari/details.html',{'sports':sports})

"""def ligue(request):
    ligue = Ligue.all()
    return render(request,'app_pari/ligue.html',{'ligue':ligue})"""

def success(request):
    g_ticket = mix()
    return render(request,'app_pari/success.html',{'g_ticket':g_ticket})
def lose(request):
    g_ticket = mix()
    return render(request,'app_pari/lose.html',{'g_ticket':g_ticket})
   
def register(request):
    form = Form_register()
    if request.method == 'POST':
        
        form = Form_register(request.POST)
        if form.is_valid():
            new_user = User(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['first_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                username=form.cleaned_data['username'],
            )
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # message = messages.success(request,'inscription reussi pour {}'.format(new_user.username))
            return redirect('app_pari:connect')
        else:
            form = Form_register()
    return render(request,'app_pari/register.html',{'form':form})

#login
def my_login(request):
    if request.POST:
        #print('is post')
        form = Form_login(request.POST)
        if form.is_valid():
            #print('is valid')
            #print(form.cleaned_data['password'])
            user = authenticate(request=request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                #print('is not none')
                login(request,user)
                return redirect('app_pari:sport')
            else:
                #print('is none')  
                return redirect('app_pari:connect')
                
        else:
            #print('is not valid')
            return redirect('app_pari:connect')
    else:
        #print('is not post')
        form = Form_login()
        return render(request,'app_pari/login.html',{'form':form})
#logout
def my_logout(request):
    logout(request)
    return redirect('home')  

def choice(request):
    if request.POST:
        form = Form_choice(request.POST)
        if form.is_valid():
            print('form valid')
            ticket = form.cleaned_data['ticket']
            g_ticket = mix()
            if ticket == g_ticket:
                print('success')
                return redirect('app_pari:success')
            else:
                #print('lose')
                return redirect('app_pari:lose')
        else:
            #print('not valid')
            return redirect('app_pari:choice')
    else:
        #print('not post')
        form = Form_choice()
        return render(request,'app_pari/choice.html',{'form':form})
        

#Generateur du chiffre aleatoire
def mix():
    lettre = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chiffre = random.randint(10,99)
    alpha=random.sample(lettre,3)
    liste=list(str(chiffre))
    liste+=list(alpha)
    random.shuffle(liste)                  
    return ''.join(liste)


  
           
            
            
        
    
    
    
    


