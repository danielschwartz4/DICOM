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

class FilterInstanceAPIView(ListAPIView):
    """This endpoint lists all of the available instances from the database"""
    serializer_class = InstanceSerializer

    def get_queryset(self):
        req = self.request.GET
        queryset = Instance.objects.all()
        
        if len(req) == 0:
            return Instance.objects.all()
        if 'q' in req:
            queryset = queryset.filter(patient_name__regex=r'\b(?i)' + req['q'])
        if 'modality' in req:
            queryset = queryset.filter(modality=req['modality'])
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