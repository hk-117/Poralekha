from django.contrib import admin
from .models import Tutor,Student,Tution,TutionRequests

# Register your models here.
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Tution)
admin.site.register(TutionRequests)
