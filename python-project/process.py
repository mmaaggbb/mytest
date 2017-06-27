进程信息 (部分os包)

Python的os包中有查询和修改进程信息的函数。学习Python的这些工具也有助于理解Linux体系。

1、进程信息

os包中相关函数如下：

(1)、uname() 返回操作系统相关信息。类似于Linux上的uname命令。

(2)、umask() 设置该进程创建文件时的权限mask。类似于Linux上的umask命令

(3)、get() 查询 (由以下代替)

uid, euid, resuid, gid, egid, resgid ：权限相关，其中resuid主要用来返回saved UID

pid, pgid, ppid, sid                 ：进程相关


(4)、put*() 设置 (*由以下代替)

euid, egid： 用于更改euid，egid。

uid, gid  ： 改变进程的uid, gid。只有super user才有权改变进程uid和gid (意味着要以$sudo python的方式运行Python)。

pgid, sid ： 改变进程所在的进程组(process group)和会话(session)。


(5)、getenviron()：获得进程的环境变量

(6)、setenviron()：更改进程的环境变量

例1，进程的real UID和real GID：

import os
print(os.getuid())
print(os.getgid())
将上面的程序保存为py_id.py文件，分别用\$python py_id.py和\$sudo python py_id.py看一下运行结果。

2、saved UID和saved GID

我们希望saved UID和saved GID如我们在Linux用户与“最小权限”原则中描述的那样工作，但这很难。原因在于，当我们写一个Python脚本后，我们实际运行的是python这个解释器，而不是Python脚本文件。对比C，C语言直接运行由C语言编译成的执行文件。我们必须更改python解释器本身的权限来运用saved UID机制，然而这么做又是异常危险的。

比如说，我们的python执行文件为/usr/bin/python (你可以通过$which python获知)

我们先看一下：

$ls -l /usr/bin/python
的结果：

-rwxr-xr-x root root
我们修改权限以设置set UID和set GID位 (参考Linux用户与“最小权限”原则)：

$sudo chmod 6755 /usr/bin/python

/usr/bin/python的权限成为:

-rwsr-sr-x root root
随后，我们运行文件下面test.py文件，这个文件可以是由普通用户所有:

import os
print(os.getresuid())
我们得到结果：(1000, 0, 0)

上面分别是UID，EUID，saved UID。我们只用执行一个由普通用户拥有的python脚本，就可以得到super user的权限！所以，这样做是极度危险的，我们相当于交出了系统的保护系统。想像一下Python强大的功能，别人现在可以用这些强大的功能作为攻击你的武器了！使用下面命令来恢复到从前:

$sudo chmod 0755 /usr/bin/python
关于脚本文件的saved UID/GID，更加详细的讨论见：http://www.faqs.org/faqs/unix-faq/faq/part4/section-7.html

五、多进程初步 (multiprocessing包)

我们已经见过了使用subprocess包来创建子进程，但这个包有两个很大的局限性：

(1) 我们总是让subprocess运行外部的程序，而不是运行一个Python脚本内部编写的函数。

(2) 进程间只通过管道进行文本交流。以上限制了我们将subprocess包应用到更广泛的多进程任务。(这样的比较实际是不公平的，因为subprocessing本身就是设计成为一个shell，而不是一个多进程管理包)。

1、threading和multiprocessing

multiprocessing包是Python中的多进程管理包。与threading.Thread类似，它可以利用multiprocessing.Process对象来创建一个进程。该进程可以运行在Python程序内部编写的函数。该Process对象与Thread对象的用法相同，也有start(), run(), join()的方法。此外multiprocessing包中也有Lock/Event/Semaphore/Condition类 (这些对象可以像多线程那样，通过参数传递给各个进程)，用以同步进程，其用法与threading包中的同名类一致。所以，multiprocessing的很大一部份与threading使用同一套API，只不过换到了多进程的情境。

但在使用这些共享API的时候，我们要注意以下几点:

在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie)。所以，有必要对每个Process对象调用join()方法 (实际上等同于wait)。对于多线程来说，由于只有一个进程，所以不存在此必要性。

multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。应优先考虑Pipe和Queue，避免使用 Lock/Event/Semaphore/Condition等同步方式 (因为它们占据的不是用户进程的资源)。

多进程应该避免共享资源。在多线程中，我们可以比较容易地共享资源，比如使用全局变量或者传递参数。在多进程情况下，由于每个进程有自己独立的内存空间，以上方法并不合适。此时我们可以通过共享内存和Manager的方法来共享资源。但这样做提高了程序的复杂度，并因为同步的需要而降低了程序的效率。

Process.PID中保存有PID，如果进程还没有start()，则PID为None。

我们可以从下面的程序中看到Thread对象和Process对象在使用上的相似性与结果上的不同。各个线程和进程都做一件事：打印PID。但问题是，所有的任务在打印的时候都会向同一个标准输出(stdout)输出。这样输出的字符会混合在一起，无法阅读。使用Lock同步，在一个任务输出完成之后，再允许另一个任务输出，可以避免多个任务同时向终端输出。

# Similarity and difference of multi thread vs. multi process
# Written by Vamei

import os
import threading
import multiprocessing

# worker function
def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()

# Main
print('Main:',os.getpid())

# Multi-thread
record = []
lock  = threading.Lock()
for i in range(5):
    thread = threading.Thread(target=worker,args=('thread',lock))
    thread.start()
    record.append(thread)

for thread in record:
    thread.join()

# Multi-process
record = []
lock = multiprocessing.Lock()
for i in range(5):
    process = multiprocessing.Process(target=worker,args=('process',lock))
    process.start()
    record.append(process)

for process in record:
    process.join()
所有Thread的PID都与主程序相同，而每个Process都有一个不同的PID。
