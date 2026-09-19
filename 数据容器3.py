#集合（不支持下标索引，无序
#1.定义集合
my_set={"福州大学","中秋","国庆","不连放"}#内容无序，不可重复
my_set_empty=set()
print(f"my_set的内容是：{my_set},类型是{type(my_set)}")
print(f"my_set_empty的内容是{my_set_empty},类型为{type(my_set_empty)}")

#添加新元素add
my_set.add("太坏了！")
print(f"{my_set}")

#移除元素remove
my_set.remove("福州大学")
print(f"{my_set}")

#随机取出一个元素pop
element=my_set.pop()
print(f"被取出的元素为{element},而集合变为{my_set}")

#清空clear
my_set.clear()
print(f"{my_set}")

#取2个集合的差集（集合一独有的那一部分，集合本身不变
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(f"set1与set2的差集为{set3}")

#消除2个集合的差集
set1.difference_update(set2)
print(f"{set1},{set2}")
#只有set1内容被改变，set2内容完全不变

#2个集合合并为1个
#重复的的地方会删掉，不可重复
set1={1,2,3}
set3=set1.union(set2)
print(f"set1{set1},set2{set2},set3{set3}")

#统计元素数量
set1={1,2,3,4,5}
num=len(set1)
print(f"{num}个")

#集合遍历
set={1,2,3,4,5}
for element in set:
    print(f"有{element}个")

#作业
#my_list=["福州大学","不连放","太坏啦","太坏啦","sobad","sobad"]
#my_set1=set()
#for element in my_list:
   # my_set1.add(element)
#print(f"列表的内容为{my_list}")
#print(f"通过for循环后，得到的集合对象为{my_set1}")

#字典
#定义
my_dict={"王力宏":99,"周杰伦":88,"林俊杰":77}
my_dict2={}
my_dict3=dict()
print(f"字典1的内容为：{my_dict}")
print(f"字典2的内容为：{my_dict2}")
print(f"字典3的内容为：{my_dict3}")

#字典的key不可重复
my_dict1={"王":99,"王":88,"李":33}#取后面那个
print(f"重复key字典部分内容为{my_dict1}")

#从字典中基于key获取value
#不可用下标索引
my_dict4={"王":99,"林":88,"李":33}
score=my_dict4["李"]
print(f"李的成绩为：{score}")

#定义嵌套字典
#key和value可以为任意数据类型（key不可以为字典
stu_score_dict={
    "王":{
        "语文":77,
        "数学":66,
        "英语":33},
    "周":{"语文":88,
        "数学":86,
        "英语":55},
    "林":{"语文":99,
        "数学":96,
        "英语":66}
}
print(f"学生考试信息为{stu_score_dict}")


#从嵌套字典中获取数据
score1=stu_score_dict["周"]["语文"]
print(f"周的语文成绩为{score1}")