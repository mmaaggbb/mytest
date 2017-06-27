#!/usr/bin/env python
#encoding:utf-8

(1)、subprocess.call()

父进程等待子进程完成

返回退出信息(returncode，相当于exit code)

(2)、subprocess.check_call()

父进程等待子进程完成

返回0

检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try...except...来检查(见Python错误处理)。

(3)、subprocess.check_output()

父进程等待子进程完成

返回子进程向标准输出的输出结果

检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性和output属性，output属性为标准输出的输出结果，可用try...except...来检查。

这三个函数的使用方法相类似，我们以subprocess.call()来说明:

import subprocess
rc = subprocess.call(["ls","-l"])
我们将程序名(ls)和所带的参数(-l)一起放在一个表中传递给subprocess.call()

可以通过一个shell来解释一整个字符串:

import subprocess
out = subprocess.call("ls -l", shell=True)
out = subprocess.call("cd ..", shell=True)
我们使用了shell=True这个参数。这个时候，我们使用一整个字符串，而不是一个表来运行子进程。Python将先运行一个shell，再用这个shell来解释这整个字符串。

shell命令中有一些是shell的内建命令，这些命令必须通过shell运行，$cd。shell=True允许我们运行这样一些命令


