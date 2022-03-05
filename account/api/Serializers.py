from asyncore import write
import email
from tkinter.ttk import Style
from rest_framework import serializers
from management.models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField( write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kargs = {
            'password':{'write_only':True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'password did not match'})
        user.set_password(password)
        user.save()
        return user