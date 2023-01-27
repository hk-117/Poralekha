from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import InfoFAQs

class FaqListView(ListView):
    model=InfoFAQs
    context_object_name = 'faqList'
