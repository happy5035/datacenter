# -*-coding:utf-8-*-
from django.db import models

__author__ = 'XJTU_YJW'


class EndDevice(models.Model):
    class Meta:
        db_table = 'end_device'

    end_device_id = models.CharField(max_length=16, db_column='end_device_id', primary_key=True)
    ext_addr = models.CharField(max_length=16, db_column='ext_addr')
    net_addr = models.CharField(max_length=4, db_column='net_addr')
    name = models.CharField(max_length=255, db_column='name')
    start_time = models.DateTimeField(db_column='start_time')
    hum_freq = models.IntegerField(db_column='hum_freq')
    temp_freq = models.IntegerField(db_column='temp_freq')
    status = models.IntegerField(db_column='status')
    voltage = models.FloatField(db_column='voltage')
    temp = models.FloatField(db_column='temp')
    hum = models.FloatField(db_column='hum')


class Temperature(models.Model):
    class Meta:
        db_table = 'temperature'

    temp_id = models.CharField(max_length=11, db_column='temp_id', primary_key=True)
    end_device = models.ForeignKey(EndDevice)
    temp_value = models.FloatField(db_column='temp_value')
    temp_time = models.DateTimeField(db_column='temp_time')


class Humidity(models.Model):
    class Meta:
        db_table = 'humidity'

    humi_id = models.CharField(max_length=11, db_column='humi_id', primary_key=True)
    end_device = models.ForeignKey(EndDevice)
    humi_value = models.FloatField(db_column='humi_value')
    humi_time = models.DateTimeField(db_column='humi_time')

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
