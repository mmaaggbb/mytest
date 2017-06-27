Pipe和Queue

管道PIPE和消息队列message queue，multiprocessing包中有Pipe类和Queue类来分别支持这两种IPC机制。Pipe和Queue可以用来传送常见的对象。

(1)、 Pipe可以是单向(half-duplex)，也可以是双向(duplex)。我们通过mutiprocessing.Pipe(duplex=False)创建单向管道 (默认为双向)。一个进程从PIPE一端输入对象，然后被PIPE另一端的进程接收，单向管道只允许管道一端的进程输入，而双向管道则允许从两端输入。

下面的程序展示了Pipe的使用:

# Multiprocessing with Pipe
# Written by Vamei

import multiprocessing as mul

def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:',pipe.recv())

def proc2(pipe):
    print('proc2 rec:',pipe.recv())
    pipe.send('hello, too')

# Build a pipe
pipe = mul.Pipe()

# Pass an end of the pipe to process 1
p1   = mul.Process(target=proc1, args=(pipe[0],))
# Pass the other end of the pipe to process 2
p2   = mul.Process(target=proc2, args=(pipe[1],))
p1.start()
p2.start()
p1.join()
p2.join()
这里的Pipe是双向的。

Pipe对象建立的时候，返回一个含有两个元素的表，每个元素代表Pipe的一端(Connection对象)。我们对Pipe的某一端调用send()方法来传送对象，在另一端使用recv()来接收。

(2)、 Queue与Pipe相类似，都是先进先出的结构。但Queue允许多个进程放入，多个进程从队列取出对象。Queue使用mutiprocessing.Queue(maxsize)创建，maxsize表示队列中可以存放对象的最大数量。

下面的程序展示了Queue的使用:

# Written by Vamei
import os
import multiprocessing
import time
#==================
# input worker
def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.time())
    queue.put(info)

# output worker
def outputQ(queue,lock):
    info = queue.get()
    lock.acquire()
    print (str(os.getpid()) + '(get):' + info)
    lock.release()
#===================
# Main
record1 = []   # store input processes
record2 = []   # store output processes
lock  = multiprocessing.Lock()    # To prevent messy print
queue = multiprocessing.Queue(3)

# input processes
for i in range(10):
    process = multiprocessing.Process(target=inputQ,args=(queue,))
    process.start()
    record1.append(process)

# output processes
for i in range(10):
    process = multiprocessing.Process(target=outputQ,args=(queue,lock))
    process.start()
    record2.append(process)

for p in record1:
    p.join()

queue.close()  # No more object will come, close the queue

for p in record2:
    p.join()
一些进程使用put()在Queue中放入字符串，这个字符串中包含PID和时间。另一些进程从Queue中取出，并打印自己的PID以及get()的字符串。
