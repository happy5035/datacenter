# -*-coding:utf-8-*-
from django.db import models

__author__ = 'XJTU_YJW'


class Room(models.Model):
    class Meta:
        db_table = 'room'
        verbose_name = '房间'
        verbose_name_plural = '房间'

    room_id = models.IntegerField(primary_key=True, db_column='room_id')
    room_name = models.CharField(db_column='room_name', max_length=255)
    room_size = models.IntegerField(db_column='room_size')
    room_x = models.IntegerField(db_column='room_x')
    room_y = models.FloatField(db_column='room_y')
    room_z = models.FloatField(db_column='room_z')
    room_x_nums = models.IntegerField(db_column='room_x_nums')
    room_y_nums = models.IntegerField(db_column='room_y_nums')
    room_pos = models.CharField(db_column='room_pos', max_length=255)


class RoomAxis(models.Model):
    class Meta:
        db_table = 'room_axis'
        verbose_name = '房间坐标'
        verbose_name_plural = '房间坐标'

    room_axis_id = models.AutoField(primary_key=True, auto_created=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    x_num = models.IntegerField()
    x_value = models.IntegerField()
    y_num = models.IntegerField()
    y_value = models.IntegerField()
    z_num = models.IntegerField()
    z_value = models.IntegerField()
    note = models.CharField(max_length=255)

    def __repr__(self):
        return '(%d,%d,%d)' % (self.x_num, self.y_num, self.z_num)

    def __str__(self):
        return '(%2d,%2d,%2d)' % (self.x_num, self.y_num, self.z_num)


class EndDevice(models.Model):
    class Meta:
        db_table = 'end_device'
        verbose_name = '终端设备'
        verbose_name_plural = '终端设备'
        ordering = ['code']

    axis = models.ForeignKey(RoomAxis, on_delete=models.CASCADE)
    end_device_id = models.CharField(max_length=16, db_column='end_device_id', primary_key=True)
    ext_addr = models.CharField(max_length=16, db_column='ext_addr')
    net_addr = models.CharField(max_length=4, db_column='net_addr')
    name = models.CharField(max_length=255, db_column='name', default='')
    start_time = models.DateTimeField(db_column='start_time')
    hum_freq = models.IntegerField(db_column='hum_freq')
    temp_freq = models.IntegerField(db_column='temp_freq')
    status = models.IntegerField(db_column='status')
    voltage = models.FloatField(db_column='voltage')
    temp = models.FloatField(db_column='temp')
    hum = models.FloatField(db_column='hum')
    update_time = models.DateTimeField(db_column='update_time')
    code = models.IntegerField()
    rssi = models.IntegerField()
    lqi = models.IntegerField()
    parent = models.CharField(max_length=4, db_column='parent')
    time_window = models.IntegerField(db_column='time_window')
    e_type = models.IntegerField(db_column='type')

    def __repr__(self):
        return '%d' % self.code

    def __str__(self):
        return '%d' % self.code


class RouterDevice(models.Model):
    class Meta:
        db_table = 'router_device'
        verbose_name = '路由器'
        verbose_name_plural = '路由器'

    axis = models.ForeignKey(RoomAxis, on_delete=models.CASCADE)
    router_device_id = models.CharField(max_length=16, db_column='router_device_id', primary_key=True)
    ext_addr = models.CharField(max_length=16, db_column='ext_addr')
    net_addr = models.CharField(max_length=4, db_column='net_addr')
    name = models.CharField(max_length=255, db_column='name', default='')
    start_time = models.DateTimeField(db_column='start_time')
    status = models.IntegerField(db_column='status')
    voltage = models.FloatField(db_column='voltage')
    update_time = models.DateTimeField(db_column='update_time')
    code = models.IntegerField()
    rssi = models.IntegerField()
    lqi = models.IntegerField()
    parent = models.CharField(max_length=4, db_column='parent')


class Temperature(models.Model):
    class Meta:
        db_table = 'temperature'
        verbose_name = '温度数据'
        verbose_name_plural = '温度数据'

    temp_id = models.CharField(max_length=11, db_column='temp_id', primary_key=True)
    end_device = models.ForeignKey(EndDevice, on_delete=models.CASCADE)
    temp_value = models.FloatField(db_column='temp_value')
    temp_time = models.DateTimeField(db_column='temp_time')


class Humidity(models.Model):
    class Meta:
        db_table = 'humidity'
        verbose_name = '温度数据'
        verbose_name_plural = '温度数据'

    humi_id = models.CharField(max_length=11, db_column='humi_id', primary_key=True)
    end_device = models.ForeignKey(EndDevice, on_delete=models.CASCADE)
    humi_value = models.FloatField(db_column='humi_value')
    humi_time = models.DateTimeField(db_column='humi_time')


class EndDeviceInfo(models.Model):
    class Meta:
        db_table = 'end_device_info'

    end_device_info_id = models.AutoField(primary_key=True, db_column='end_device_info_id')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    end_device_code = models.IntegerField()
    end_device = models.ForeignKey(EndDevice, related_name='info', on_delete=models.CASCADE)
    x_pos_name = models.CharField(max_length=255)
    x_pos_value = models.IntegerField()
    y_pos_name = models.CharField(max_length=255)
    y_pos_value = models.IntegerField()
    z_temp_name = models.CharField(max_length=255)
    z_temp_value = models.IntegerField()
    status = models.IntegerField()


class NetParam(models.Model):
    class Meta:
        db_table = 'net_param'
        verbose_name = '网络参数'
        verbose_name_plural = '网络参数'

    net_param_id = models.AutoField(primary_key=True)
    panid = models.CharField(max_length=4)
    pv = models.IntegerField()
    chanel = models.IntegerField()
    temp_freq = models.IntegerField()
    hum_freq = models.IntegerField()
    packet_freq = models.IntegerField()
    clock_freq = models.IntegerField()
    time_window_internal = models.IntegerField()

    pass


class CabinetPos(models.Model):
    class Meta:
        db_table = 'cabinet_pos'
        verbose_name = '机柜位置信息'
        verbose_name_plural = '机柜位置信息'
        ordering = ['cabinet_row', 'cabinet_num', 'cabinet_unum', 'front_back']

    cabinet_pos_id = models.AutoField(primary_key=True)
    cabinet_row = models.IntegerField()
    cabinet_num = models.IntegerField()
    cabinet_unum = models.IntegerField()
    room_name = models.IntegerField()
    front_back = models.IntegerField()
    note = models.CharField(max_length=255)


class EndCabinetRelation(models.Model):
    class Meta:
        db_table = 'end_cabinet_relation'
        verbose_name = '终端机柜位置信息'
        verbose_name_plural = '终端机柜位置信息'

    end_cabinet_relation_id = models.AutoField(primary_key=True)
    end_device = models.ForeignKey(EndDevice, on_delete=models.CASCADE)
    cabinet = models.ForeignKey(CabinetPos, db_column='start_cabinet_id')
    add_time = models.DateTimeField(auto_now=True)
