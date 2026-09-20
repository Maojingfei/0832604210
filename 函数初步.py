def check():
    print("福州大学\n数字媒体技术")
check()

def add(x,y):#x,y为形参,而且可以有更多个
    print(f"{x} + {y} 的计算结果为 = {x+y}")
add(996,123)#996,123为实参

#作业
print("欢迎来到福州大学，请配合测量体温！")
tem = float(input("您的体温监测为："))
def check(tem):
    if tem<=37.5:
        print(f"您的体温为{tem},体温正常请进！")
    else:
        print(f"您的体温为：{tem} ,体温过高.需要隔离！")
check(tem)


def add(x,y):
    result = x + y
    return result #结果返回调用者
    #return下侧的代码不会执行
result=add(12,23)
print(result)

def say_hi():
    print("你好呀！")
result = say_hi() #函数没有返回值return,所以result为None
print(result) #输出None
print(f"result的类型为：{type(result)}") #输出None的类型

#在if判断中，None被认为是False

def add(x,y):
    """
    add函数的作用是将两个数相加
    :param x:形参第一个数
    :param y:形参第二个数
    :return: 返回两数相加的结果
    """
    #：param指的是参数的说明
    
    result = x + y
    print(f"两数相加的结果是{result}")
    return result
add(5,6)#鼠标悬停有注释

def func_b():
    print("---2---")
def func_a():
    print("---1---")
    func_b()
    print("---3---")
func_a()#函数嵌套

def test_a():
    num=100#局部变量,在函数内部使用
    print(num)
test_a()

num=200#外部可使用，全局变量
def test_a():
    print(f"test_a:{num}")
def test_b():#可以局部修改 同时加入局部变量num=500
    print(f"test_b:{num}")
test_a()
test_b()
print(num)
#global关键字可以在函数内部修改全局变量****



