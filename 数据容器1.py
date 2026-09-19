#1.字面量 
#[元素1,元素2,元素3]

#2.定义元素
#变量名 = [元素1,元素2,元素3]

##3.定义空列表
##变量名=[]
##变量名=list()

my_list=["mao","jingfei","xiaoming"]
print(my_list)
print(type(my_list))

my_list2=["mao",123,True,3.14]
print(my_list2)
print(type(my_list2))

my_list3=[[1,2,3],[4,5,6]]#列表嵌套
print(my_list3)
print(type(my_list3))

#下标索引[0,1,2,3,...]or[...,-4,-3,-2,-1]
my_list4=["mao","jingfei","xiaoming"]
print(my_list4[0])# 输出: mao
print(my_list4[1])# 输出: jingfei
print(my_list4[2])# 输出: xiaoming

print(my_list4[-1])# 输出: xiaoming
print(my_list4[-2])# 输出: jingfei

my_list5=[[1,2,3],[4,5,6]]
print(my_list5[0][0])#****

#index()方法：返回指定元素在列表中索引值
my_list6=["mao","jingfei","xiaoming"]
index=my_list6.index("mao")#返回索引值0
print(f"mao在列表中的索引值为：{index}")

#修改列表：列表[下标]=值
my_list6[0]="gagaga"
print(f"修改后的列表为：{my_list6}")

#insert()方法：在指定位置插入元素
my_list6.insert(1,666)#把后面那个元素插到前面那个指定位置的数字
print(f"插入元素后的列表为：{my_list6}")

#append()方法：在列表末尾添加元素
my_list6.append("mememe")
print(f"在列表末尾添加元素后的列表为：{my_list6}")

#extend()方法：在列表末尾添加另一个列表的所有元素
my_list6.extend([1,2,3])
print(f"在列表末尾添加另一个列表的所有元素后的列表为：{my_list6}")

my_list7=["yi","er",3,4]
#del列表[下标]：删除指定下标的元素
del my_list7[1]
print(f"删除元素后的列表为：{my_list7}")
#列表.pop(下标)：删除指定下标的元素，并返回该元素
element = my_list7.pop(1)#可以通过返回得到
print(f"通过pop方法被删除元素后列表内容：{my_list7}，被删除的元素为：{element}")
#列表.remove(元素)：删除指定元素
my_list7.remove("yi")#一次只能删除一个元素哦
print(f"通过remove方法删除元素后的列表为：{my_list7}")
#del pop 指定下标删除，而remove指定元素删除
my_list7.clear()
print(f"清空列表后的列表为：{my_list7}")#清空

#统计列表中指定元素的个数
my_list8=["mao","jingfei","xiaoming","mao"]
count = my_list8.count("mao")
print(f"元素'mao'在列表中出现的次数为：{count}")

#统计列表内所有元素数量
my_list9=["mao","jingfei","xiaoming","mao"]
count=len(my_list9)
print(f"列表中所有元素的数量为：{count}")

#作业
list=[21,25,21,23,22,20]
list.append(31)
list.extend([29,33,30])
print(list[0])
print(list[-1])
index=list.index(31)
print(f"31在列表中的索引值为：{index}")
