from django.urls import path
from account.api.views import *

app_name = 'account'



urlpatterns = [
    path('register', regestration_view, name='register'),
]