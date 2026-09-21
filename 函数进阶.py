#return语句多次返回方法
def test_return():
    return 1,"中秋放假",True
x,y,z=test_return()
print(x)
print(y)
print(z)

#多种传参方式
def user_info(name,age,gender):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")

#位置参数：调用函数时根据函数定义的 参数位置来传递参数
user_info("小美","66","男")

#关键字参数
user_info(name="小赵",age=99,gender="女")
user_info(gender="女",name="小赵",age=99)#可乱序

#缺省参数（默认值
def user_info(name,age,gender="男"):#有默认值，但是可以通过后续推翻，若无则为默认
     print(f"姓名是：{name},年龄是：{age},性别是：{gender}")
#设置默认值必须在末尾，或者末尾几个全都默认
user_info("嘎嘎嘎",10)#默认男
user_info("咕咕咕",12,"女")#结果为女

#不定长参数

#不定长-位置不定长 *号
#不定长的定义形式参数会作为 元组tuple 存在
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容为：{args}")

user_info(1,2,3,"毛毛",True,666)

#不定长-关键词不定长 **号
#不定长的定义形式参数会作为 字典dict 存在
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)},内容为：{kwargs}")
    #数量不受限，但是必须有key,有value
user_info(name="毛小毛",age=12,height=180)#要用=哦

#定义一个函数，接受另一个函数作为传入函数
def test_func(computer):
    result=computer(19999,20996756)#确定computer为函数
    print(f"computer参数的类型为:{type(computer)},计算结果为{result}")
#定义另一个参数，准备作为参数传入另一个函数
def computer(x,y):
    return x+y
#调用并传入
test_func(computer)

#lambda匿名函数
#lambda 传入参数:函数体(一行代码)
def test_func(compute):
    result=compute(1,2)
    print(f"结果是{result}")#定义一个函数
test_func(lambda x,y:x**y)#连return都可以省略#函数体不可写多行