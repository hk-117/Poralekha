from django.urls import path
from .views import FaqListView
from . import views

urlpatterns=[
    path('',FaqListView.as_view(template_name='discussion/faqs.html'),name='discussion-faqs'),
]
