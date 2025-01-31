from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('login/', views.login_view, name='login-view'),
    path('sign-up/', views.signup_view, name='signup-view'),
    path('logout/', views.logout_view, name='logout'),
]