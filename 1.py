#获取姓名
name = input('你的名字：') 
#获取身高
high = input('你的身高：')
#获取年龄
age = input('你的年龄：')
#获取体重
weight = input('你的体重：')
#新建文件保存信息
f = open('%s.txt'%name,'w')
#输出信息到文件
print('==========\n姓名:%s\n身高:%s\n年龄:%s\n体重:%s\n=========='%(name,high,age,weight),file=f)
