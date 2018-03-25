# -*- coding: utf-8 -*-
from datacenter.models import *

num = 16
unum = 42
row_nums = 8
cab_list = []
for k in range(row_nums):
    cabinet_row = k + 1
    for i in range(num):
        for j in range(unum):
            c = CabinetPos()
            c.room_name = '21'
            c.cabinet_row = cabinet_row
            c.cabinet_num = i + 1
            c.cabinet_unum = j + 1
            c.front_back = 0
            cab_list.append(c)
            c = CabinetPos()
            c.room_name = '21'
            c.cabinet_row = cabinet_row
            c.cabinet_num = i + 1
            c.cabinet_unum = j + 1
            c.front_back = 1
            cab_list.append(c)
        pass
CabinetPos.objects.bulk_create(cab_list)
print('over')
