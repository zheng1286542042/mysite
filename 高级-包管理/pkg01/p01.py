# 包含一个学生类，
# 一个sayhello函数
# 一个打印语句

class Student():
    def __init__(self, name="NoName", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("hi ,欢迎来到图灵学院")

print("我是模块p01呀，你叫我干啥")


