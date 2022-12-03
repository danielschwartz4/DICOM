from rest_framework import serializers
from instance.models import Instance

class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = "__all__" 
				 