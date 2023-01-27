from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserForm,TutorUpForm,StudentUpForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from main.models import Tutor,Student
from poralekha.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def verify(request):
    if request.method=='POST':
        email= request.POST['email']
        usertype=request.POST['usertype']
        domain=request.get_host()
        route='/users/register?email='+email+'&usertype='+ usertype
        subject="Welcome to poralekha.com!!!"
        message="Click on the link to register :"+"http://"+domain+route
        send_mail(subject,message,EMAIL_HOST_USER,[email,],fail_silently=False)
        return render(request,'users/register_steptwo.html')
    return render(request,'users/register_stepone.html')

def register(request):
    if request.method=='POST':
        userform=UserForm(request.POST)
        usertype=request.POST['usertype']
        email=request.POST['email']
        if usertype=='T':
            form=TutorUpForm(request.POST,request.FILES)
        else:
            form=StudentUpForm(request.POST,request.FILES)
        if userform.is_valid() and form.is_valid():
            messages.success(request,f"Account has been created ! Login Now!!!")
            userCreate= userform.save(commit=False)
            userCreate.email=email
            userCreate.first_name=usertype
            userCreate.save()
            profileCreate=form.save(commit=False)
            profileCreate.username=userCreate
            profileCreate.save()
            return redirect(reverse('homepage'))
        else:
            messages.error(request,f"Fill up the form Correctly")
    else:
        email=request.GET['email']
        usertype = request.GET['usertype']
        userform=UserForm()
        if usertype=='T':
            form=TutorUpForm()
        else:
            form=StudentUpForm()
    context={
        'email':email,
        'usertype':usertype,
        'userform':userform,
        'form':form,
    }
    return render(request,'users/register.html',context)

@login_required
def update(request):
    if request.method=='POST':
        userinstance=request.user
        usertype=userinstance.first_name
        userform=UserUpdateForm(request.POST,instance=userinstance)
        if usertype=='T':
            profile=Tutor.objects.filter(username=userinstance).first()
            form=TutorUpForm(request.POST,request.FILES,instance=profile)
        else:
            profile=Student.objects.filter(username=userinstance).first()
            form=StudentUpForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and form.is_valid():
            userform.save()
            form.save()
            messages.success(request,f"Account Updated Successfully")
            return redirect(reverse('profile'))
        else:
            messages.error(request,f"Fill up the form Correctly")
    else:
        userinstance=request.user
        usertype=userinstance.first_name
        userform=UserUpdateForm(instance=userinstance)
        if usertype=='T':
            profile=Tutor.objects.filter(username=userinstance).first()
            form=TutorUpForm(instance=profile)
        else:
            profile=Student.objects.filter(username=userinstance).first()
            form=StudentUpForm(instance=profile)
    context={
        'usertype':usertype,
        'userform':userform,
        'form':form,
    }
    return render(request,'users/update.html',context)
