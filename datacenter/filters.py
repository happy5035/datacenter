# -*- coding: utf-8 -*-
import django_filters
from datacenter.models import *
from django_filters import rest_framework as filters


class HumidityFilter(django_filters.FilterSet):
    min_humi_value = filters.NumberFilter(name='humi_value', lookup_expr='gte')
    max_humi_value = filters.NumberFilter(name='humi_value', lookup_expr='lte')
    humi_time = filters.DateTimeFromToRangeFilter(name='humi_time')
    ext_addr = filters.CharFilter(name='end_device__ext_addr')

    class Meta:
        model = Humidity
        fields = ['min_humi_value', 'max_humi_value', 'humi_time']


class TemperatureFilter(django_filters.FilterSet):
    min_temp_value = filters.NumberFilter(name='temp_value', lookup_expr='gte')
    max_temp_value = filters.NumberFilter(name='temp_value', lookup_expr='lte')
    temp_time = filters.DateTimeFromToRangeFilter(name='temp_time')
    end_device_id = filters.CharFilter(field_name='end_device__end_device_id')

    class Meta:
        model = Temperature
        fields = ['min_temp_value', 'max_temp_value', 'temp_time']


class EndDeviceFilter(django_filters.FilterSet):
    ext_addr = filters.CharFilter(name='ext_addr')
    net_addr = filters.CharFilter(name='net_addr')
    status = filters.NumberFilter(name='status')
    voltage_min = filters.NumberFilter(name='voltage', lookup_expr='gte')
    voltage_max = filters.NumberFilter(name='voltage', lookup_expr='lte')
    hum_freq = filters.NumberFilter(name='hum_freq')
    temp_freq = filters.NumberFilter(name='temp_freq')
    start_time = filters.DateTimeFromToRangeFilter(name='start_time')

    class Meta:
        model = EndDevice
        fields = ['ext_addr', 'net_addr', 'status', 'voltage', 'hum_freq', 'temp_freq', 'start_time']


class RouterDeviceFilter(django_filters.FilterSet):
    ext_addr = filters.CharFilter(name='ext_addr')
    net_addr = filters.CharFilter(name='net_addr')
    status = filters.NumberFilter(name='status')
    voltage_min = filters.NumberFilter(name='voltage', lookup_expr='gte')
    voltage_max = filters.NumberFilter(name='voltage', lookup_expr='lte')
    start_time = filters.DateTimeFromToRangeFilter(name='start_time')

    class Meta:
        model = EndDevice
        fields = ['ext_addr', 'net_addr', 'status', 'voltage', 'start_time']


class EndDeviceInfoFilter(django_filters.FilterSet):
    class Meta:
        model = EndDeviceInfo
        fields = []
