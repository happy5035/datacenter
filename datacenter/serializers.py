# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from datacenter.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = ('humi_id', 'humi_time', 'humi_value')

    pass


class EndDeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndDeviceInfo
        fields = ('__all__')


class RoomAxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAxis
        fields = (
            '__all__')


class EndDeviceSerializer(serializers.ModelSerializer):
    axis = RoomAxisSerializer()

    class Meta:
        model = EndDevice
        fields = (
            '__all__')


class TemperatureSerializer(serializers.ModelSerializer):
    end_device = EndDeviceSerializer()

    class Meta:
        model = Temperature
        fields = (
            '__all__')


class NetParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetParam
        fields = (
            '__all__')
