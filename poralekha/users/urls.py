from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
    path('verify/',views.verify,name='user-mail-verify'),
    path('register/',views.register,name='user-register'),
    path('update/',views.update,name='user-update'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name="users-login"), 
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name="users-logout"), 
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]
