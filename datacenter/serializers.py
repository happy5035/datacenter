# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from datacenter.models import EndDevice, Humidity, Temperature, Snippet


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


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('temp_id', 'temp_time', 'temp_value')


class EndDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndDevice
        fields = (
            'end_device_id', 'net_addr', 'ext_addr', 'name', 'voltage', 'start_time', 'hum_freq', 'temp_freq', 'status')


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
