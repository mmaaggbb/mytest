实际上，我们上面的三个函数都是基于Popen()的封装(wrapper)。这些封装的目的在于让我们容易使用子进程。当我们想要更个性化我们的需求的时候，就要转向Popen类，该类生成的对象用来代表子进程。

与上面的封装不同，Popen对象创建后，主程序不会自动等待子进程完成。我们必须调用对象的wait()方法，父进程才会等待 (也就是阻塞block)：

import subprocess
child = subprocess.Popen(["ping","-c","5","www.google.com"])
print("parent process")
从运行结果中看到，父进程在开启子进程之后并没有等待child的完成，而是直接运行print。

对比等待的情况:

import subprocess
child = subprocess.Popen(["ping","-c","5","www.google.com"])
child.wait()
print("parent process")
此外，你还可以在父进程中对子进程进行其它操作，比如我们上面例子中的child对象:

child.poll() # 检查子进程状态

child.kill() # 终止子进程

child.send_signal() # 向子进程发送信号

child.terminate() # 终止子进程

子进程的PID存储在child.pid。

3、子进程的文本流控制

(沿用child子进程) 子进程的标准输入，标准输出和标准错误也可以通过如下属性表示:

child.stdin
child.stdout
child.stderr
我们可以在Popen()建立子进程的时候改变标准输入、标准输出和标准错误，并可以利用subprocess.PIPE将多个子进程的输入和输出连接在一起，构成管道(pipe):

import subprocess
child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=subprocess.PIPE)
out = child2.communicate()
print(out)
subprocess.PIPE实际上为文本流提供一个缓存区。child1的stdout将文本输出到缓存区，随后child2的stdin从该PIPE中将文本读取走。child2的输出文本也被存放在PIPE中，直到communicate()方法从PIPE中读取出PIPE中的文本。

要注意的是，communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成。

我们还可以利用communicate()方法来使用PIPE给子进程输入:

import subprocess
child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
child.communicate("vamei")
我们启动子进程之后，cat会等待输入，直到我们用communicate()输入"vamei"。

通过使用subprocess包，我们可以运行外部程序。这极大的拓展了Python的功能。如果你已经了解了操作系统的某些应用，你可以从Python中直接调用该应用(而不是完全依赖Python)，并将应用的结果输出给Python，并让Python继续处理。shell的功能(比如利用文本流连接各个应用)，就可以在Python中实现
