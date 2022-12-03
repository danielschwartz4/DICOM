from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from instance.serializers import InstanceSerializer
from instance.models import Instance

# Create your views here.
class ListInstanceAPIView(ListAPIView):
    """This endpoint list all of the available instances from the database"""
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

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