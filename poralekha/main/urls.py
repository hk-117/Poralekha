from django.urls import path,include
from . import views
from .views import (
        TutorListView,
        TutorDetailView,
        CircularListView,
        CircularDetailView,
        StudentDetailView
        )

urlpatterns=[
    path('',views.index,name='homepage'),
    path('profile/',views.profile,name='profile'),
    path('faqs/',include('discussion.urls')),
    path('users/',include('users.urls')),
    path('about/',views.about_us,name='about-us'),
    path('tutors/',TutorListView.as_view(),name='tutor-list'),
    path('tutors/<int:pk>',TutorDetailView.as_view(),name='tutor-detail'),
    path('circulars/',CircularListView.as_view(),name='circular-list'),
    path('circulars/<int:pk>',CircularDetailView.as_view(),name='circular-detail'),
    path('circulars/<int:pk>/update',views.updateTution,name='circular-update'),
    path('circulars/<int:pk>/delete',views.deleteTution,name='circular-delete'),
    path('circulars/<int:pk>/requests',views.requests,name='circular-requests'),
    path('circulars/<int:pk>/finish',views.finishTution,name='circular-finish'),
    path('circulars/<int:pk>/apply',views.applyTution,name='circular-apply'),
    path('circulars/new/',views.createCircular,name='circular-new'),
    path('students/<int:pk>',StudentDetailView.as_view(),name='student-detail'),
    path('sent-message/',views.sentMessage,name='sent-message'),
]
