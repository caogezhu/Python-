greet = "您好，崩坏：星穹铁道"
print(greet + "希儿")

# 对字符串求长度
s = "Hello World"
print(len(s))

# 通过索引获取单个字符
print(s[0])
print(s[len(s) - 1])

#布尔类型
b1 = True
b2 = False

#空值类型
n = None

# type函数
print(type(s))
print(type(b1))
print(type(n))
print(type(1.5))

import math

a = 1
b = 9
c = 20
delta = b ** 2 - 4 * a * c
print((-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a))