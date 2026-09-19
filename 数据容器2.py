def list_while_func():
    my_list=["福州大学","程序员","Python"]
    index=0
    while index<len(my_list):
        element=my_list[index]
        print(f"列表的元素：{element}")
        index+=1
list_while_func()

#tuple元组
#定义
t1=(True,"程序员","Python")
t2=()
t3=tuple()
print(f"t1的类型是{type(t1)},内容是{t1}")
print(f"t2的类型是{type(t2)},内容是{t2}")
print(f"t3的类型是{type(t3)},内容是{t3}")

t4=("Hello")#如果是单个元素的元组，必须在元素后面加上逗号才是tuple，否则会被当作普通数据类型
print(f"t4的类型是{type(t4)},内容是{t4}")
t4=("Hello",)
print(f"t4的类型是{type(t4)},内容是{t4}")

t5=((1,2,3),("a","b","c"))
print(f"t5的类型是{type(t5)},内容是{t5}")

#下标索引取出内容，与list列表相同
num=t5[1][2]
print(f"从嵌套元组中取出的数据为：{num}")

#index()  count()  len(元组)
t6=("mao",666,True,"Python","程序员")#查找元素下标索引
index=t6.index("Python")
print(f"Python在t6元组中的下标索引为：{index}")

num=t6.count("程序员")#统计元素出现的次数
print(f"程序员在t6元组中出现的次数为：{num}")

num=len(t6)#统计元组中元素的个数
print(f"t6元组中元素的个数为：{num}")


#元素遍历 while
index=0
while index<len(t6):
    print(f"元组的元素有:{t6[index]}")
    index+=1

for element in t6:
    print(f"元组的元素有：{element}")

#split:按指定的分隔符字符串，分割为多个字符串
my_str="hello python guoqinfanjia hhhhh"
my_str_list=my_str.split()
print(f"分割的结果是：{my_str_list}")

#strip（）  去前后空隔
#字符串.strip(字符串)   去掉前后指定的字符串

#字符串的替换   字符串.replace(字符串1，字符串2)
str666="嘎嘎嘎guaguagua666"
new_str666=str666.replace("guaguagua","hhhhhhh")
print(f"修改后的str666为：{new_str666}")
#切片：从一个序列中，取出一个字序列
#序列[起始下标：结束下标：步长]
#起始下标可以留空，即从头开始，结束下标（不含）表示何处结束，可以留空，即为截到结尾
#对list切片
my_list=[0,1,2,3,4,5,6]
result1=my_list[1:4:1]#指的是第几个
print(f"结果1：{result1}")

#对tuple切片
my_tuple=(0,1,2,3,4,5,6)
result2=my_tuple[:]#从头到尾
print(f"结果2为：{result2}")

my_str="01234567"
result3=my_str[::2]
print(f"结果3为{result3}")

#作业
str="！休双我还，你厌讨学大州福，课上末周"
result4=str[::-1][13:17]
result5=result4.split()
print(f"{result5}")