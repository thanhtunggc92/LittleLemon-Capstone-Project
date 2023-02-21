from rest_framework import serializers
from .models import Menu,Booking
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields ='__all__'


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','group']

class Bookingserializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'





