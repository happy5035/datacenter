# -*- coding: utf-8 -*-
from django.shortcuts import render
import django_filters.rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from datacenter.serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from datacenter.filters import *
from django_filters.rest_framework import DjangoFilterBackend


def test(request):
    return render(request, 'index1.html')
    pass
def echart_test(request):
    return render(request,'test.html')


def socket_test(request):
    return render(request, 'socket.html')


class HumidityList(generics.ListAPIView):
    queryset = Humidity.objects.all().order_by('humi_time')
    serializer_class = HumiditySerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = HumidityFilter
    pass


class TemperatureList(generics.ListAPIView):
    queryset = Temperature.objects.all().order_by('temp_time')
    serializer_class = TemperatureSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = TemperatureFilter


class EndDeviceList(generics.ListAPIView):
    queryset = EndDevice.objects.all()
    serializer_class = EndDeviceSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = EndDeviceFilter


class HumidityDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer
    pass


class TemperatureDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    pass


class EndDeviceDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = EndDevice.objects.all()
    serializer_class = EndDeviceSerializer
    pass


def humidity_list(request):
    if request.method == 'GET':
        humiditys = Humidity.objects.all()
        serializer = HumiditySerializer(humiditys, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HumiditySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    pass


def temperature_list(request):
    if request.method == 'GET':
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TemperatureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    pass


def end_device_list(request):
    if request.method == 'GET':
        end_devices = EndDevice.objects.all()
        serializer = EndDeviceSerializer(end_devices, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EndDeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    pass


def humidity_detail(request, pk):
    try:
        humidity = Humidity.objects.get(humi_id=pk)
    except Humidity.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = HumiditySerializer(humidity)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HumiditySerializer(humidity, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)
    elif request.method == 'DELETE':
        humidity.delete()
        return HttpResponse(status=204)


def temperature_detail(request, pk):
    try:
        temperature = Temperature.objects.get(temp_id=pk)
    except Temperature.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = TemperatureSerializer(temperature)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Temperature(temperature, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)
    elif request.method == 'DELETE':
        temperature.delete()
        return HttpResponse(status=204)


def end_device_detail(request, pk):
    try:
        end_device = EndDevice.objects.get(end_device_id=pk)
    except EndDevice.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = EndDeviceSerializer(end_device)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EndDeviceSerializer(end_device, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)
    elif request.method == 'DELETE':
        end_device.delete()
        return HttpResponse(status=204)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
