from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, UpdateAPIView)
from django_filters import rest_framework as filters
from instance.models import Instance
from instance.serializers import InstanceSerializer


# Create your views here.
class FilterInstanceAPIView(ListAPIView):
    """This endpoint lists all of the available instances from the database"""
    serializer_class = InstanceSerializer

    def get_queryset(self):
        if 'q' in self.request.GET:
            # lookup_url_kwarg = "instance"
            # patient_name = self.kwargs.get(self.lookup_url_kwarg)
            # queryset = Instance.objects.filter(patient_name__regex=r'\b(?i)' + patient_name)
            queryset = Instance.objects.filter(patient_name__regex=r'\b(?i)' + self.request.GET['q'])
        else:
            queryset = Instance.objects.all() 
        return queryset

class ListInstanceAPIView(ListAPIView):
    """This endpoint lists all of the available instances from the database"""
    serializer_class = InstanceSerializer
    lookup_url_kwarg = "instance"
    
    def get_queryset(self):
        print(self.kwargs)
        patient_name = self.kwargs.get(self.lookup_url_kwarg)
        print(patient_name)
        queryset = Instance.objects.filter(patient_name__regex=r'\b(?i)' + patient_name)
        return queryset

class CreateInstanceAPIView(CreateAPIView):
    """This endpoint allows for creation of an instance"""
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

class UpdateInstanceAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific instance by passing in the id of the instance to update"""
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

class DeleteInstanceAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Instance from the database"""
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer