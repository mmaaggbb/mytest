#!/usr/bin/env python
#encoding:utf-8


#库程序TestLib.py。当直接运行TestLib.py时，__name__为"__main__"。如果被import的话，__name__为"TestLib"。
#查询函数的参数
import inspect
print(inspect.getargspec(func))
#查询对象的属性
dir(object)
bool s=hasattr(obj, attr_name)
#
#查询对象所属的类和类名称
a = [1, 2, 3]
print a.__class__
print a.__class__.__name__
#
#查询父类
cls.__base__
#
#使用中文
#coding=utf8
#-*- coding: UTF-8 -*-

#表示2进制，8进制和16进制数字
print(0b1110)     # 二进制，以0b开头
print(0o10)       # 八进制，以0o开头
print(0x2A)       # 十六进制，以0x开头
#脚本与命令行结合
$python -i script.py
#内置函数
#数学运算
#
abs(-5)                          # 取绝对值，也就是5
round(2.6)                       # 四舍五入取整，也就是3.0
pow(2, 3)                        # 相当于2**3，如果是pow(2, 3, 5)，相当于2**3 % 5
cmp(2.3, 3.2)                    # 比较两个数的大小
divmod(9,2)                      # 返回除法结果和余数
max([1,5,2,9])                   # 求最大值
min([9,2,-4,2])                  # 求最小值
sum([2,-1,9,12])                 # 求和

#类型转换
int("5")                         # 转换为整数 integer
float(2)                         # 转换为浮点数 float
long("23")                       # 转换为长整数 long integer
str(2.3)                         # 转换为字符串 string
complex(3, 9)                    # 返回复数 3 + 9i

ord("A")                         # "A"字符对应的数值
chr(65)                          # 数值65对应的字符
unichr(65)                       # 数值65对应的unicode字符

bool(0)                          # 转换为相应的真假值，在Python中，0相当于False .在Python中，下列对象都相当于False：** [], (), {}, 0, None, 0.0, '' **

bin(56)                          # 返回一个字符串，表示56的二进制数
hex(56)                          # 返回一个字符串，表示56的十六进制数
oct(56)                          # 返回一个字符串，表示56的八进制数

list((1,2,3))                    # 转换为表 list
tuple([2,3,4])                   # 转换为定值表 tuple
slice(5,2,-1)                    # 构建下标对象 slice
dict(a=1,b="hello",c=[1,2,3])    # 构建词典 dictionary

#序列操作
all([True, 1, "hello!"])         # 是否所有的元素都相当于True值
any(["", 0, False, [], None])    # 是否有任意一个元素相当于True值

sorted([1,5,3])                  # 返回正序的序列，也就是[1,3,5]
reversed([1,5,3])                # 返回反序的序列，也就是[3,5,1]
#类、对象、属性
#
# define class
class Me(object):
    def test(self):
        print "Hello!"

def new_test():
    print "New Hello!"

me = Me()

hasattr(me, "test")               # 检查me对象是否有test属性
getattr(me, "test")               # 返回test属性
setattr(me, "test", new_test)     # 将test属性设置为new_test
delattr(me, "test")               # 删除test属性
isinstance(me, Me)                # me对象是否为Me类生成的对象 (一个instance)
issubclass(Me, object)            # Me类是否为object类的子类


#编译、执行
repr(me)                          # 返回对象的字符串表达
compile("print('Hello')",'test.py','exec')       # 编译字符串成为code对象
eval("1 + 1")                     # 解释字符串表达式。参数也可以是compile()返回的code对象
exec("print('Hello')")            # 解释并执行字符串，print('Hello')。参数也可以是compile()返回的code对象
#
#其他
input("Please input:")            # 等待输入

globals()                         # 返回全局命名空间，比如全局变量名，全局函数名
locals()                          # 返回局部命名空间
#
#字符串格式化
print("I'm %s. I'm %d year old" % ('Vamei', 99))
#
a = "I'm %s. I'm %d year old" % ('Vamei', 99)
print(a)
#
print("I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99})
#
#格式符
#
%s    字符串 (采用str()的显示)
%r    字符串 (采用repr()的显示)
%c    单个字符
%b    二进制整数
%d    十进制整数
%i    十进制整数
%o    八进制整数
%x    十六进制整数
%e    指数 (基底写为e)
%E    指数 (基底写为E)
%f    浮点数
%F    浮点数，与上相同
%g    指数(e)或浮点数 (根据显示长度)
%G    指数(E)或浮点数 (根据显示长度)

%%    字符"%"

%[(name)][flags][width].[precision]typecode
#(name)为命名
#flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
#width表示显示宽度
#precision表示小数点后精度
#
print("%+10x" % 10)
print("%04d" % 5)
print("%6.3f" % 2.3)
#
print("%.*f" % (4, 1.2))
#
#
#
#
#
#
#
#
#
#
#
#
