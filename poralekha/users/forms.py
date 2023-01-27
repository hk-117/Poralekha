from main.models import Tutor,Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.forms import ModelForm
from main import commons as Z

class UserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email= models.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class TutorUpForm(ModelForm):

    def clean_preffered_subject(self):
        data=self.cleaned_data.get('preffered_subject')
        preffered_subject=""
        for c in data:
            if c not in ['[',']','\'']:
                preffered_subject+= c
        return preffered_subject
    
    def clean_preffered_medium(self):
        data=self.cleaned_data.get('preffered_medium')
        preffered_medium=""
        for c in data:
            if c not in ['[',']','\'']:
                preffered_medium+= c
        return preffered_medium

    def clean_preffered_class(self):
        data=self.cleaned_data.get('preffered_class')
        preffered_class=""
        for c in data:
            if c not in ['[',']','\'']:
                preffered_class+= c
        return preffered_class

    def clean_preffered_time(self):
        data=self.cleaned_data.get('preffered_time')
        preffered_time=""
        for c in data:
            if c not in ['[',']','\'']:
                preffered_time+= c
        return preffered_time
    class Meta:
        model=Tutor
        exclude=[
            'username',
            'is_premium',
            'rating',
            'tution_status',
            'current_tution_number',
            'total_tution_so_far',
            ]
        widgets={
            'gender': forms.Select(choices=Z.GENDER),
            'qualification': forms.Select(choices=Z.QUALIFICATIONS),
            'preffered_subject': forms.SelectMultiple(choices=Z.SUBJECTS),
            'preffered_medium': forms.SelectMultiple(choices=Z.MEDIUM),
            'preffered_class': forms.SelectMultiple(choices=Z.CLASS),
            'preffered_time': forms.SelectMultiple(choices=Z.TIME),
            'address_division':forms.Select(choices=Z.DIVISIONS),
            'address_district':forms.Select(choices=Z.DISTRICTS),
        }

class StudentUpForm(ModelForm):

    class Meta:
        model=Student
        exclude=['username']
        widgets={
            'address_division':forms.Select(choices=Z.DIVISIONS),
            'address_district':forms.Select(choices=Z.DISTRICTS),
            'info_class': forms.Select(choices=Z.CLASS),
            'info_medium': forms.Select(choices=Z.MEDIUM), 
            'info_gender': forms.Select(choices=Z.GENDER),
        }
