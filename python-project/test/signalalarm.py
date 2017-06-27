#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import signal
def myHandler(signum,frame):
	print("时间到！！！")
	exit()
signal.signal(signal.SIGALRM,myHandler)
signal.alarm(5)
while True:
	print('not yet')
