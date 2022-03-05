from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User

from account.api.Serializers import *


@api_view(['POST'])
def regestration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "sucessfully regesterd a new user"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return response(serializer.data)
