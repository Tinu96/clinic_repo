from rest_framework import serializers
from customer.models import *

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Services
        fields="__all__"

class BeauticianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Beautician
        fields="__all__"

class TimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Timeslots
        fields="__all__"

class BookingSerializer(serializers.Serializer):
    fields="body"

class AddOnSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddOns
        fields="__all__"
