from django.shortcuts import render
from .models import Booking,Menu
from .serializers import MenuSerializer,Bookingserializer,Userserializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import permissions
# Create your views here.


def index(request):
    context={}
    return render(request,'index.html',context)


class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class=MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = Bookingserializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [permissions.IsAuthenticated]