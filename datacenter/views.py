# -*- coding: utf-8 -*-
from django.shortcuts import render
import django_filters.rest_framework
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from datacenter.serializers import *
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics
from datacenter.filters import *
from datacenter import params_handler
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def test(request):
    return render(request, 'index1.html')
    pass


@csrf_exempt
def set_params(request):
    data = JSONParser().parse(request)
    param = NetParam.objects.filter(net_param_id=data['net_param_id']).first()
    set_param = []
    temp_freq = int(data['temp_freq'])
    packet_freq = int(data['packet_freq'])
    clock_freq = int(data['clock_freq'])
    time_window_internal = int(data['time_window_internal'])
    pv = int(data['pv'])
    if temp_freq != param.temp_freq:
        set_param.append({'name': 'temp_freq', 'value': temp_freq})
        param.temp_freq = temp_freq
    if packet_freq != param.packet_freq:
        set_param.append({'name': 'packet_freq', 'value': packet_freq})
        param.packet_freq = packet_freq
    if clock_freq != param.clock_freq:
        set_param.append({'name': 'clock_freq', 'value': clock_freq})
        param.clock_freq = clock_freq
    if time_window_internal != param.time_window_internal:
        set_param.append({'name': 'time_window_internal', 'value': time_window_internal})
        param.time_window_internal = time_window_internal
    if len(set_param):
        param.pv = pv + 1
        param.save()
        params_handler.send_params({'pv': pv + 1, 'param': set_param})
        pass
    return JsonResponse({'result': 'success'})
    pass


def end_device_tooltip(request, pk):
    end_device = EndDevice.objects.filter(end_device_id=pk).first()
    end_device.update_time = end_device.update_time.strftime('%Y-%m-%d %H:%M:%S')
    end_device.net_addr = end_device.net_addr.upper()
    end_device.net_addr = '0X%s%s' % (end_device.net_addr[2:], end_device.net_addr[:2])
    ed_info = EndDeviceInfo.objects.filter(end_device_id=end_device.end_device_id).first()

    return render(request, 'end_device_tooltip.html', {'ed': end_device, 'info': ed_info})
    pass


def echart_test(request):
    return render(request, 'test.html')


def socket_test(request):
    return render(request, 'socket.html')


def diagrapm(request, pk):
    data = {'end_device_id': pk}
    # return render(request, 'hello.html', data)
    return render(request, 'end_device_diagram.html', data)


def diagrapm_3D(request, pk):
    data = {'end_device_id': pk}
    # return render(request, 'hello.html', data)
    return render(request, 'end_device_3d.html', data)


def nodes(request):
    return render(request, 'end_device_nodes.html')


def nodes_fix(request):
    net_param = NetParam.objects.all().first()

    return render(request, 'end_device_nodes_fix.html', {'net_param': net_param})


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
    queryset = EndDevice.objects.all().order_by('code')
    serializer_class = EndDeviceSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class RouterDeviceList(generics.ListAPIView):
    queryset = RouterDevice.objects.all()
    serializer_class = RouterDeviceSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class NetParamList(generics.ListAPIView):
    queryset = NetParam.objects.all()
    serializer_class = NetParamSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class EndDeviceInfoList(generics.ListAPIView):
    queryset = EndDeviceInfo.objects.all()
    serializer_class = EndDeviceInfoSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = EndDeviceInfoFilter

    pass


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


class RouterDeviceDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = RouterDevice.objects.all()
    serializer_class = RouterDeviceSerializer
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

def end_device_page_list(request,page,num):
    if request.method == 'GET':
        end_devices = EndDevice.objects.all()
        paginator = Paginator(end_devices, int(num))
        try:
            end_devices_page = paginator.page(int(page))
        except PageNotAnInteger:
            end_devices_page = paginator.page(1)
        except EmptyPage:
            end_devices_page = paginator.page(paginator.num_pages)
        end_devices = end_devices_page.object_list
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

def router_device_list(request):
    if request.method == 'GET':
        router_device = RouterDevice.objects.all()
        serializer = RouterDeviceSerializer(router_device, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RouterDeviceSerializer(data=data)
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




def router_device_detail(request, pk):
    try:
        router_device = RouterDevice.objects.get(router_device_id=pk)
    except RouterDevice.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = RouterDeviceSerializer(router_device)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RouterDeviceSerializer(router_device, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)
    elif request.method == 'DELETE':
        router_device.delete()
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
