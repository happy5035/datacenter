# -*- coding: utf-8 -*-

from django.contrib import admin
from datacenter.models import *


class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('net_addr', 'ext_addr', 'temp_time', 'temp_value')
    list_filter = ('temp_time',)
    search_fields = ['end_device__net_addr', 'end_device__ext_addr']
    show_full_result_count = 30

    def net_addr(self, temp):
        return temp.end_device.net_addr

    def ext_addr(self, temp):
        return temp.end_device.ext_addr

    def temp_time(self, temp):
        return temp.temp_time


class EndDeviceAdmin(admin.ModelAdmin):
    exclude = ('end_device_id',)
    list_display = ('ext_addr', 'net_addr', 'voltage', 'temp', 'hum', 'hum_freq', 'temp_freq', 'status', 'update_time')


admin.site.register(Temperature, TemperatureAdmin)
admin.site.register(EndDevice, EndDeviceAdmin)
admin.site.register(Humidity)
