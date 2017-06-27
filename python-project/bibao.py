#!/usr/bin/env python
#encoding:utf-8
#需求：通过闭包对一个数据 x 做“流水线操作”，至少三层闭包，每一层依次进行一项操作，
#
#闭包


def xiangfan(x):
    def kaifang(x):
        def juedui(x):
            return abs(x)
        return juedui(x)**0.5
    return -kaifang(x)

print xiangfan(-4)

#装饰器
def juedui(x):
    return abs(x)

def kaifang(F):
    def new_F(x):
        return F(x)**0.5
    return new_F

def xiangfan(F):
    def new_F(x):
        return -F(x)
    return new_F

func=xiangfan(kaifang(juedui))

print func(-4)
