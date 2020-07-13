'''
import math
print("math")
# ceil()向上取整操作
print(math.ceil(5.01))
#
# floor()向下取整操作
print(math.floor(5.9))

# round()四舍五入
print(round(5.1))
print(round(5.5))

# sqrt()开平方，返回浮点数
print(math.sqrt(4))


# pow()与幂运算差不多，计算一个数的几次方
print(math.pow(4, 3))
# 幂运算，函数返回浮点型，幂运算返回整形
print(4**3)

# fabs() 对一个数字获取绝对值,返回的浮点数
print(math.fabs(-1))

# abs() 对一个数字获取绝对值，不是数学模块中的，是python内置函数,返回值由本身类型决定
print(abs(-1))

# fsum()对整个序列求和,返回浮点数
print(math.fsum([1, 4, 5, 5, 7]))

# sum() python内置求和，返回值由本身类型决定
print(sum([1, 4, 5, 5, 7]))

# math.modf() 将一个浮点数拆分为整数部分和小数部分组成元组，小数在前，整数在后
print(math.modf(4.5))
print(math.modf(3))

# copysign() 将第二个数的符号传给第一个数,返回第一个数值的浮点数
print(math.copysign(2, -3))

# 打印自认对数e 和π的值
print(math.e)
print(math.pi)
'''

import random
# random() 获取0-1之前的随机小数，不包含1
for i in range(10):
    print(random.random())
    # 随机指定开始和结束指定的值，包含开始和结束
    print(random.randint(1, 9))
    # random.randrange() 获取指定开始和结束之前的值，可以指定间隔值
    print(random.randrange(1, 9, 3))
    # uniform() 随机获取指定范围内的值(包括小数)
    print(random.uniform(1, 9))

# choice() 随机获取列表中的值
print(random.choice([1,3,367,86]))
# shuffle() 随机打乱序列，返回值为None
list1 = [1,5,367,86]
print(list1)
random.shuffle(list1)
print(list1)















