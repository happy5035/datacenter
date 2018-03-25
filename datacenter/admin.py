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


class EndCabinetRelation(admin.TabularInline):
    model = EndCabinetRelation
    exclude = ('end_cabinet_relation_id',)


class EndDeviceInfoInline(admin.TabularInline):
    model = EndDeviceInfo
    exclude = ('end_device_info_id',)
    extra = 0
    pass


class EndDeviceAdmin(admin.ModelAdmin):
    # inlines = [EndCabinetRelation, ]
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


class CabinetRowListFilter(admin.SimpleListFilter):
    title = ('机柜列位置')
    parameter_name = 'row'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        rows = []
        for cp in qs:

            if cp.cabinet_row in rows:
                pass
            else:
                rows.append(cp.cabinet_row)
        for r in rows:
            yield (r, (chr(r + 64)))
        pass

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(cabinet_row=self.value())
        else:
            return queryset


class CabinetNumListFilter(admin.SimpleListFilter):
    title = ('机柜编号')
    parameter_name = 'num'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        rows = []
        for cp in qs:

            if cp.cabinet_num in rows:
                pass
            else:
                rows.append(cp.cabinet_num)
        for r in rows:
            yield (r, (chr(r + 64)))
        pass

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(cabinet_num=self.value())
        else:
            return queryset


class CabinetUNumListFilter(admin.SimpleListFilter):
    title = ('机柜U编号')
    parameter_name = 'num'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        rows = []
        for cp in qs:

            if cp.cabinet_unum in rows:
                pass
            else:
                rows.append(cp.cabinet_unum)
        for r in rows:
            yield (r, ('%sU' % r))
        pass

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(cabinet_unum=self.value())
        else:
            return queryset


class RouterDeviceAdmin(admin.ModelAdmin):
    # inlines = [EndDeviceInfoInline, ]
    view_on_site = True
    exclude = ('router_device_id',)
    # search_fields = ['code']
    list_display = (
        'ext_addr', 'code', 'net_addr', 'voltage', 'update_time', 'axis')
    fields = (
        'code', 'axis', 'ext_addr', 'net_addr', 'voltage' 'status', 'update_time', 'parent')

    list_filter = ('ext_addr',)


class CabinetPosAdmin(admin.ModelAdmin):
    exclude = ('cabinet_pos_id',)
    inlines = (EndCabinetRelation,)
    list_display = ('name', 'room_name', 'cabinet_row_name', 'cabinet_num_name', 'cabinet_unum_name', 'front_back1')
    fields = ('room_name', 'cabinet_row', 'cabinet_num', 'cabinet_unum')
    list_filter = (CabinetRowListFilter, CabinetNumListFilter, CabinetUNumListFilter)

    def name(self, m: CabinetPos):
        if m.front_back == 0:
            return '%s-%s%s%sU 前' % (m.room_name, chr(m.cabinet_row + 64), chr(m.cabinet_num + 64), m.cabinet_unum)
        else:
            return '%s-%s%s%sU 后' % (m.room_name, chr(m.cabinet_row + 64), chr(m.cabinet_num + 64), m.cabinet_unum)

    name.short_description = '编号位置'

    def cabinet_row_name(self, m: CabinetPos):
        return chr(m.cabinet_row + 64)

    cabinet_row_name.short_description = '列编号'

    def cabinet_num_name(self, m: CabinetPos):
        return chr(m.cabinet_num + 64)

    cabinet_num_name.short_description = '机柜编号'

    def cabinet_unum_name(self, m: CabinetPos):
        return '%sU' % m.cabinet_unum

    cabinet_unum_name.short_description = 'U编号'

    def front_back1(self, m: CabinetPos):
        if m.front_back == 0:
            return '前面'
        if m.front_back == 1:
            return '背面'

    front_back1.short_description = '面'


admin.site.register(Temperature, TemperatureAdmin)
admin.site.register(EndDevice, EndDeviceAdmin)
# admin.site.register(EndDeviceInfo, EndDeviceInfoAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(NetParam, NetParamAdmin)
admin.site.register(RoomAxis, RoomAxisAdmin)
admin.site.register(RouterDevice, RouterDeviceAdmin)
admin.site.register(CabinetPos, CabinetPosAdmin)
# admin.site.register(Humidity)
