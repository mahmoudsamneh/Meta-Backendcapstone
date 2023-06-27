from django.shortcuts import render
from rest_framework import generics , viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# The views

def index(request):
    return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        queryset = Booking.objects.all().values('name')
        serializer = BookingSerializer(queryset, many = True)
        return Response(serializer.data) 
    
        
        