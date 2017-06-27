#!/usr/bin/env python
#encoding:utf-8

os.path包
import os.path
path = '/home/vamei/doc/file.txt'

print(os.path.basename(path))    # 查询路径中包含的文件名
print(os.path.dirname(path))     # 查询路径中包含的目录

info = os.path.split(path)       # 将路径分割成文件名和目录两个部分，放在一个表中返回
path2 = os.path.join('/', 'home', 'vamei', 'doc', 'file1.txt')  # 使用目录名和文件名构成一个路径字符串

p_list = [path, path2]
print(os.path.commonprefix(p_list))    # 查询多个路径的共同部分

os.path.normpath(path)   # 去除路径path中的冗余。比如'/home/vamei/../.'被转化为'/home'
import os.path 
path = '/home/vamei/doc/file.txt'

print(os.path.exists(path))    # 查询文件是否存在

print(os.path.getsize(path))   # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取的时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间

print(os.path.isfile(path))    # 路径是否指向常规文件
#
#
print(os.path.isdir(path))     # 路径是否指向目录文件

mkdir(path) 创建新目录，path为一个字符串，表示新目录的路径。相当于$mkdir命令

rmdir(path) 删除空的目录，path为一个字符串，表示想要删除的目录的路径。相当于$rmdir命令

listdir(path) 返回目录中所有文件。相当于$ls命令。

remove(path) 删除 path指向的文件。

rename(src, dst) 重命名文件，src和dst为两个路径，分别表示重命名之前和之后的路径。

chmod(path, mode) 改变path指向的文件的权限。相当于$chmod命令。

chown(path, uid, gid) 改变path所指向文件的拥有者和拥有组。相当于$chown命令。

stat(path) 查看path所指向文件的附加信息，相当于$ls -l命令。

symlink(src, dst) 为文件dst创建软链接，src为软链接文件的路径。相当于$ln -s命令。

getcwd() 查询当前工作路径 (cwd, current working directory)，相当于$pwd命令


shutil包

copy(src, dst) 复制文件，从src到dst。相当于$cp命令。

move(src, dst) 移动文件，从src到dst。相当于$mv命令。

import shutil
shutil.copy('a.txt', 'b.txt')

pickle包
将内存中的对象转换成为文本流
import pickle

# define class
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

summer       = Bird()                 # construct an object
picklestring = pickle.dumps(summer)   # serialize object
###########################################################################################
对象summer存储在文件a.pkl
import pickle

# define class
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

summer       = Bird()                        # construct an object
fn           = 'a.pkl'
with open(fn, 'w') as f:                     # open file with write-mode
    picklestring = pickle.dump(summer, f)   # serialize and save object

###########################################################################################
重建对象
import pickle

# define the class before unpickle
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

fn     = 'a.pkl'
with open(fn, 'r') as f:
    summer = pickle.load(f)   # read file and build object

cPickle包的功能和用法与pickle包几乎完全相同 (其存在差别的地方实际上很少用到)，不同在于cPickle是基于c语言编写的，速度是pickle包的1000倍。对于上面的例子，如果想使用cPickle包，我们都可以将import语句改为:

import cPickle as pickle











