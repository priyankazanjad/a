from django.urls import path
from . import views

urlpatterns=[
    path('reg/',views.registerView,name='register'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
]