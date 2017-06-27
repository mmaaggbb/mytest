#!/usr/bin/env python
#encoding:utf-8

时间与日期
import time
print(time.time())   # wall clock time, unit: second
print(time.clock())  # processor clock time, unit: second

import time
print('start')
time.sleep(10)     # sleep for 10 seconds
print('wake up')


st = time.gmtime()      # 返回struct_time格式的UTC时间
st = time.localtime()   # 返回struct_time格式的当地时间, 当地时区根据系统环境决定。

s  = time.mktime(st)    # 将struct_time格式转换成wall clock time

datetime

import datetime
t = datetime.datetime(2012,9,3,21,30)
print(t)
hour, minute, second, microsecond
year, month, day, weekday   # weekday表示周几

运算
import datetime
t      = datetime.datetime(2012,9,3,21,30)
t_next = datetime.datetime(2012,9,5,23,30)
delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
print(t + delta1)
print(t + delta2)
print(t_next - t)

datetime对象与字符串转换

from datetime import datetime
format = "output-%Y-%m-%d-%H%M%S.txt" 
str    = "output-1997-12-23-030000.txt" 
t      = datetime.strptime(str, format)


