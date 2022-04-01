from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonModelForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import auth

def registerView(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    template_name='UserApp/register.html'
    return render(request, template_name, context)

def loginView(request):
    if request.method=='POST':
        un=request.POST.get('uname')
        pw=request.POST.get('pw')
        user=authenticate(username='uname',userpassword='pw')
        if user is not None:
            login(request,user)
        else:
            messages.error(request,'invalid')
    context={}
    template_name='UserApp/login.html'
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')

def addUser(request):
    form=PersonModelForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_user')
    context={'form':form}
    template_name='UserApp/register.html'
    return render(request, template_name, context)

def final(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        pw = request.POST.get('pw')
        user = authenticate(username='uname', userpassword='pw')
        if user is login:
            user.objects.all()
        else:
            messages.error(request, 'invalid user')
    context = {}
    template_name = 'UserApp/errorpage.html'
    return render(request, template_name, context)







