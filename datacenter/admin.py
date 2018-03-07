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


class EndDeviceInfoAdmin(admin.ModelAdmin):
    exclude = ('end_device_info_id',)
    list_display = (
        'end_device_code', 'x_pos_name', 'x_pos_value', 'y_pos_name', 'y_pos_value', 'z_temp_name', 'z_temp_value')
    ordering = ['end_device_code', ]


class RoomAdmin(admin.ModelAdmin):
    exclude = ('room_id',)
    list_display = (
        'room_name', 'room_size', 'room_x', 'room_y', 'room_z', 'room_x_nums', 'room_y_nums', 'room_pos'
    )


class NetParamAdmin(admin.ModelAdmin):
    exclude = ('net_param_id',)
    list_display = (
        'pv', 'temp_freq', 'packet_freq', 'clock_freq'
    )


class RoomAxisAdmin(admin.ModelAdmin):
    exclude = ('room_axis_id',)
    list_display = (
        'room_id', 'x_num', 'x_value', 'y_num', 'y_value', 'z_num', 'z_value', 'note'
    )


class EndDeviceInfoInline(admin.TabularInline):
    model = EndDeviceInfo
    exclude = ('end_device_info_id',)
    extra = 0
    pass


class EndDeviceAdmin(admin.ModelAdmin):
    # inlines = [EndDeviceInfoInline, ]
    view_on_site = True
    exclude = ('end_device_id',)
    # search_fields = ['code']
    list_display = (
        'ext_addr', 'code', 'net_addr', 'voltage', 'temp', 'hum', 'hum_freq', 'temp_freq', 'update_time',
        'axis', 'test')
    fields = (
        'code', 'axis', 'ext_addr', 'net_addr', 'voltage', 'temp', 'hum', 'hum_freq', 'temp_freq', 'status',
        'update_time', 'parent', 'e_type')

    def test(self, end):
        return '<a href=/diagram/{pk}>open</a>'.format(pk=end.end_device_id)
        pass

    # def x_num(self, ed: EndDevice):
    #     return ed.axis.x_num
    #     pass

    # ordering = ['code', ]
    test.allow_tags = True
    test.short_description = 'Diagram'
    list_filter = ('ext_addr',)


admin.site.register(Temperature, TemperatureAdmin)
admin.site.register(EndDevice, EndDeviceAdmin)
# admin.site.register(EndDeviceInfo, EndDeviceInfoAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(NetParam, NetParamAdmin)
admin.site.register(RoomAxis, RoomAxisAdmin)
# admin.site.register(Humidity)
