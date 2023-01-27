from .models import Tution
from django.db import models
from django import forms
from django.forms import ModelForm
from . import commons as Z

class TutionForm(ModelForm):

    def clean_student_subjects(self):
        data=self.cleaned_data.get('student_subjects')
        student_subjects=""
        for c in data:
            if c not in ['[',']','\'']:
                student_subjects+= c
        return student_subjects

    class Meta:
        model=Tution
        exclude=[
            'posted_by',
            'tutor',
            'confirmed',
            'time_created',
            'time_confirmed',
            'time_ended',
            'rating_given',
        ]
        widgets={
            'student_class':forms.Select(choices=Z.CLASS),
            'student_medium':forms.Select(choices=Z.MEDIUM),
            'student_subjects':forms.SelectMultiple(choices=Z.SUBJECTS), 
            'student_district':forms.Select(choices=Z.DISTRICTS), 
            'student_gender':forms.Select(choices=Z.GENDER),
            'requirement_gender':forms.Select(choices=Z.PREF_GENDER),
            'requirement_teaching_time':forms.Select(choices=Z.TIME)
        }
