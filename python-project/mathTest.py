math包

math包主要处理数学相关的运算。math包定义了两个常数:

math.e   # 自然常数e
math.pi  # 圆周率pi
此外，math包还有各种运算函数 (下面函数的功能可以参考数学手册)：

math.ceil(x)       # 对x向上取整，比如x=1.2，返回2
math.floor(x)      # 对x向下取整，比如x=1.2，返回1
math.pow(x,y)      # 指数运算，得到x的y次方
math.log(x)        # 对数，默认基底为e。可以使用base参数，来改变对数的基地。比如math.log(100,10)
math.sqrt(x)       # 平方根
三角函数: math.sin(x), math.cos(x), math.tan(x), math.asin(x), math.acos(x), math.atan(x)

这些函数都接收一个弧度(radian)为单位的x作为参数。

角度和弧度互换: math.degrees(x), math.radians(x)

双曲函数: math.sinh(x), math.cosh(x), math.tanh(x), math.asinh(x), math.acosh(x), math.atanh(x)

特殊函数： math.erf(x), math.gamma(x)

2、random包

如果你已经了解伪随机数(psudo-random number)的原理，那么你可以使用如下:

random.seed(x)
来改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。

(1)、随机挑选和排序

random.choice(seq)   # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
random.sample(seq,k) # 从序列中随机挑选k个元素
random.shuffle(seq)  # 将序列的所有元素随机排序
(2)、随机生成实数

下面生成的实数符合均匀分布(uniform distribution)，意味着某个范围内的每个数字出现的概率相等:

random.random()          # 随机生成下一个实数，它在[0,1)范围内。
random.uniform(a,b)      # 随机生成下一个实数，它在[a,b]范围内。
下面生成的实数符合其它的分布 (你可以参考一些统计方面的书籍来了解这些分布):

random.gauss(mu,sigma)    # 随机生成符合高斯分布的随机数，mu,sigma为高斯分布的两个参数。 
random.expovariate(lambd) # 随机生成符合指数分布的随机数，lambd为指数分布的参数。
此外还有对数分布，正态分布，Pareto分布，Weibull分布，可参考下面链接:

http://docs.python.org/library/random.html

假设我们有一群人参加舞蹈比赛，为了公平起见，我们要随机排列他们的出场顺序。我们下面利用random包实现：

import random
all_people = ['Tom', 'Vivian', 'Paul', 'Liya', 'Manu', 'Daniel', 'Shawn']
random.shuffle(all_people)
for i,name in enumerate(all_people):
    print(i,':'+name)
三、循环器 (itertools)

在循环对象和函数对象中，我们了解了循环器(iterator)的功能。循环器是对象的容器，包含有多个对象。通过调用循环器的next()方法 (__next__()方法，在Python 3.x中)，循环器将依次返回一个对象。直到所有的对象遍历穷尽，循环器将举出StopIteration错误。

itertools的工具都可以自行实现。itertools只是提供了更加成形的解决方案。

在for i in iterator结构中，循环器每次返回的对象将赋予给i，直到循环结束。使用iter()内置函数，我们可以将诸如表、字典等容器变为循环器。比如：

for i in iter([2, 4, 5, 6]):
    print(i)
标准库中的itertools包提供了更加灵活的生成循环器的工具。这些工具的输入大都是已有的循环器。另一方面，这些工具完全可以自行使用Python实现，该包只是提供了一种比较标准、高效的实现方式。这也符合Python“只有且最好只有解决方案”的理念。

# import the tools
from itertools import *
1、无穷循环器

count(5, 2)     #从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...
cycle('abc')    #重复序列的元素，既a, b, c, a, b, c ...
repeat(1.2)     #重复1.2，构成无穷循环器，即1.2, 1.2, 1.2, ...
repeat也可以有一个次数限制:

repeat(10, 5)   #重复10，共重复5次
2、函数式工具

函数式编程是将函数本身作为处理对象的编程范式。在Python中，函数也是对象，因此可以轻松的进行一些函数式的处理，比如map(), filter(), reduce()函数。

itertools包含类似的工具。这些函数接收函数作为参数，并将结果返回为一个循环器。

比如：

from itertools import *

rlt = imap(pow, [1, 2, 3], [1, 2, 3])

for num in rlt:
    print(num)
上面显示了imap函数。该函数与map()函数功能相似，只不过返回的不是序列，而是一个循环器。包含元素1, 4, 27，即1**1, 2**2, 3**3的结果。函数pow(内置的乘方函数)作为第一个参数。pow()依次作用于后面两个列表的每个元素，并收集函数结果，组成返回的循环器。

此外，还可以用下面的函数:

starmap(pow, [(1, 1), (2, 2), (3, 3)])     #pow将依次作用于表的每个tuple。
ifilter函数与filter()函数类似，只是返回的是一个循环器。

ifilter(lambda x: x > 5, [2, 3, 5, 6, 7]) #将lambda函数依次作用于每个元素，如果函数返回True，则收集原来的元素。6, 7。
此外：

ifilterfalse(lambda x: x > 5, [2, 3, 5, 6, 7])     #与上面类似，但收集返回False的元素。2, 3, 5
takewhile(lambda x: x < 5, [1, 3, 6, 7, 1])     #当函数返回True时，收集元素到循环器。一旦函数返回False，则停止。1, 3
dropwhile(lambda x: x < 5, [1, 3, 6, 7, 1])     #当函数返回False时，跳过元素。一旦函数返回True，则开始收集剩下的所有元素到循环器。6, 7, 1
3、组合工具

我们可以通过组合原有循环器，来获得新的循环器。

chain([1, 2, 3], [4, 5, 7])      # 连接两个循环器成为一个。1, 2, 3, 4, 5, 7
product('abc', [1, 2])   # 多个循环器集合的笛卡尔积。相当于嵌套循环
for m, n in product('abc', [1, 2]):
    print m, n
permutations('abc', 2)   # 从'abc'中挑选两个元素，比如ab, bc, ... 将所有结果排序，返回为新的循环器。
注意，上面的组合分顺序，即ab, ba都返回。

combinations('abc', 2)   # 从'abcd'中挑选两个元素，比如ab, bc, ... 将所有结果排序，返回为新的循环器。
注意，上面的组合不分顺序，即ab, ba的话，只返回一个ab。

combinations_with_replacement('abc', 2) # 与上面类似，但允许两次选出的元素重复。即多了aa, bb, cc
4、groupby()

将key函数作用于原循环器的各个元素。根据key函数结果，将拥有相同函数结果的元素分到一个新的循环器。每个新的循环器以函数返回结果为标签。

这就好像一群人的身高作为循环器。我们可以使用这样一个key函数: 如果身高大于180，返回"tall"；如果身高底于160，返回"short";中间的返回"middle"。最终，所有身高将分为三个循环器，即"tall", "short", "middle"。

def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends, key = height_class)
for m, n in groupby(friends, key = height_class):
    print(m)
    print(list(n))
注意，groupby的功能类似于UNIX中的uniq命令。分组之前需要使用sorted()对原循环器的元素，根据key函数进行排序，让同组元素先在位置上靠拢。

5、其它工具

compress('ABCD', [1, 1, 1, 0])  # 根据[1, 1, 1, 0]的真假值情况，选择第一个参数'ABCD'中的元素。A, B, C
islice()                        # 类似于slice()函数，只是返回的是一个循环器
izip()                          # 类似于zip()函数，只是返回的是一个循环器。
