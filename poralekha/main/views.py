from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .models import Tutor,Student,Tution,TutionRequests
from .forms import TutionForm
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from poralekha.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .filters import TutorFilter,TutionFilter

def index(request):
    return render(request,'main/index.html',context={
        "tutors": Tutor.objects.filter(is_premium=True)[:4],
        "tutions": Tution.objects.order_by('-time_created')[:3],
    })

@login_required
def profile(request):
    usertype= request.user.first_name
    user= request.user
    template_name=''
    if usertype=='T':
        profile_data= user.tutor_set.all().first()
        template_name='main/tutor_profile.html'
        context={
            'profile_data':profile_data,
            'applied_tution':TutionRequests.objects.filter(tutor=profile_data),
            'ongoing_tution':Tution.objects.filter(tutor=profile_data,confirmed=True,ended=False),
            'finished_tution':Tution.objects.filter(tutor=profile_data,confirmed=True,ended=True),
        }
    else:
        profile_data= user.student_set.all().first()
        template_name='main/student_profile.html'
        context={
            'profile_data':profile_data,
            'posted_tution':Tution.objects.filter(posted_by=profile_data,confirmed=False),
            'ongoing_tution':Tution.objects.filter(posted_by=profile_data,confirmed=True,ended=False),
            'finished_tution':Tution.objects.filter(posted_by=profile_data,confirmed=True,ended=True),
        }
    return render(request,template_name,context)
    
def about_us(request):
    return render (request, 'main/about_us.html')

class TutorListView(ListView):
    model=Tutor
    context_object_name='tutors'
    ordering = ['-is_premium']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter']=TutorFilter(self.request.GET,queryset=self.get_queryset())
        return context

class TutorDetailView(DetailView):
    model=Tutor
    context_object_name='tutor'

class CircularListView(ListView):
    model=Tution
    context_object_name='tutions'
    ordering=['-time_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter']=TutionFilter(self.request.GET,queryset=self.get_queryset())
        return context

class CircularDetailView(DetailView):
    model=Tution
    context_object_name='tution'

class StudentDetailView(DetailView):
    model=Student
    context_object_name='student'

def sentMessage(request):
    if request.method=="POST":
        receiver_email=request.POST['receiver_email']
        sender_name=request.POST['sender_name']
        sender_phone=request.POST['sender_phone']
        sender_email=request.POST['sender_email']
        message=request.POST['message']
        subject= sender_email +" Want's to be connected "
        extra = "Name: "+ sender_name +"\n" + "Phone: "+sender_phone+"\n"+"Email: "+sender_email+"\n"
        send_mail(subject,extra+message,EMAIL_HOST_USER,[receiver_email,],fail_silently=False)
        messages.success(request,f"Email sent Successfully!")
        return redirect(reverse('homepage'))

def createCircular(request):
    if request.method=='POST':
        form=TutionForm(request.POST)
        if form.is_valid():
            circular=form.save(commit=False)
            circular.posted_by=Student.objects.filter(username=request.user).first()
            circular.time_created=datetime.now()
            circular.save()
            messages.success(request,f"Circular Creation Successful")
            return redirect(reverse('circular-list'))
        else:
            messages.error(request,f"Error")
    else:
        form=TutionForm()
    context={
        'form':form,
    }
    return render(request,'main/circular_new.html',context)

def updateTution(request,pk):
    user=request.user
    circularInstance=Tution.objects.get(pk=pk)
    if not (user.is_authenticated and user==circularInstance.posted_by.username):
        messages.error(request,f"Login as the author of this Circular!")
        return redirect('/circulars/'+str(pk))
    if request.method=="POST":
        updateform=TutionForm(request.POST,instance=circularInstance)
        if updateform.is_valid():
            updateform.save()
            messages.success(request,f"Circular Update Successful")
            return redirect('/circulars/'+str(pk))
    else:
        updateform=TutionForm(instance=circularInstance)
    context={
        'form':updateform,
        'pk':pk,
    }
    return render(request,'main/circular_update.html',context)

def deleteTution(request,pk):
    user=request.user
    circularInstance=Tution.objects.get(pk=pk)
    if not (user.is_authenticated and user==circularInstance.posted_by.username):
        messages.error(request,f"Login as the author of this Circular!")
        return redirect('/circulars/'+str(pk))
    if request.method=="POST":
        circularInstance.delete()
        messages.success(request,f"Circular Deleted Successfully")
        return redirect('/circulars/')
    context={
        'pk':pk,
    }
    return render(request,'main/circular_delete.html',context)

def requests(request,pk):
    user=request.user
    circularInstance=Tution.objects.get(pk=pk)
    if not (user.is_authenticated and user==circularInstance.posted_by.username):
        messages.error(request,f"Login as the author of this Circular!")
        return redirect('/circulars/'+str(pk))
    if request.method=="POST" and 'confirm' in request.POST:
        req_by=request.POST['req_by']
        tutor=Tutor.objects.get(pk=req_by)
        circularInstance.confirmed=True
        circularInstance.tutor=tutor
        circularInstance.time_confirmed=datetime.now()
        circularInstance.save()
        reqs=TutionRequests.objects.filter(tution=circularInstance)
        reqs.delete()
        messages.success(request,f"Confirmed")
        return redirect('/circulars/'+str(pk))
    elif request.method=="POST" and 'cancel' in request.POST:
        req_by=request.POST['req_by']
        reqs=TutionRequests.objects.filter(tution=circularInstance,tutor=req_by)
        reqs.delete()
        messages.error(request,f"Calcelled")
    reqs=circularInstance.tutionrequests_set.all()
    context={
        'requests':reqs 
    }
    return render(request,'main/requests.html',context)

def finishTution(request,pk):
    user=request.user
    circularInstance=Tution.objects.get(pk=pk)
    tutor=circularInstance.tutor
    if not (user.is_authenticated and user==circularInstance.posted_by.username):
        messages.error(request,f"Login as the author of this Circular!")
        return redirect('/circulars/'+str(pk))
    if request.method=="POST":
        rating=request.POST['rating']
        circularInstance.rating_given=rating
        circularInstance.ended=True
        circularInstance.time_ended=datetime.now()
        circularInstance.save()
        jobs=Tution.objects.filter(tutor=tutor)
        tot=0
        for j in jobs:
            tot+= j.rating_given
        rating_count=len(jobs)
        avg_rating=tot//rating_count
        tutor.rating=avg_rating
        if avg_rating >= 4:
            tutor.is_premium=True
        tutor.save()
        messages.success(request,f"Job Done Successfully")
        return redirect('/circulars/')
    context={
        'pk':pk,
    }
    return render(request,'main/circular_finish.html',context)

def applyTution(request,pk):
    user=request.user
    tutor=user.tutor_set.all().first()
    circularInstance=Tution.objects.get(pk=pk)
    req=TutionRequests.objects.filter(tutor=tutor,tution=circularInstance)
    if len(req):
        messages.error(request,f"You already applied!!!")
        return redirect('/circulars/'+str(pk))
    if request.method=="POST":
        req_new=TutionRequests(tution=circularInstance,tutor=tutor)
        req_new.save()
        messages.success(request,f"Applied Successfully!!!")
        return redirect('/circulars/')
