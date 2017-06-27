#!/usr/bin/env python
#encoding:utf-8

def decorator(F):
	def new_F(a,b):
		print("input",a,b)
		return F(a,b)
	return new_F

def square_sum(a,b):
	return a**2+b**2

def square_diff(a,b):
	return a**2-b**2

#装饰器
square=decorator(square_sum)
result1=square(3,4)
print(result1)
square=decorator(square_diff)
result2=square(4,5)
print(result2)
