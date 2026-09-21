#open(name,mode,encoding)
#name即为要打开的目标文件名字符串
#mode打开模式：(read)只读r，(write)写入w，(add)追加a
#encoding编码格式（推荐UTF-8

#打开文件
f=open("测试","r",encoding="UTF-8")
print(type(f))
#读取文件 read()
print(f.read(1))
print(f"read方法读取全部内容的结果为:{f.read()}")
print("-------------------------------------------------")

#读取文件 readlines()
lines=f.readlines()#读取文件全部行，封装到列表中
print(f"lines对象的内容为：{lines}")

#读取文件 readlines()
line1=f.readline()
line2=f.readline()
line3=f.readline()#print(f"第一行的数据是：{line1}")
print(f"第二行的数据是：{line2}")
print(f"第三行的数据是：{line3}")

#for循环读取文件行
for line in f:
    print(f"每一行数据为：{line}")

#关闭文件  
f.close()
time.sleep(500000) # type: ignore

#with open语法操作文件
import time
with open("测试","r",encoding="UTF-8")as f:
    for line in f:
        print(f"每一行数据为：{line}")
time.sleep(500000)

#作业
f=open("测试","r",encoding="UTF-8")
#方式1
content=f.read()
count=content.count("itheima")
print(f"itheima在文件里出现了：{count}次")