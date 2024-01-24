import os
import time
import random
import hashlib

def creatfile(path,size,suffix):
        tmp=time.strftime("%Y%m%d%H%M%S",time.localtime()) + str(random.random())
        name=hashlib.md5(tmp.encode('utf-8')).hexdigest()
        name=name+suffix
        if(path==''): 
                bigFile= open(name,'w',encoding='utf-8')
        else:
                bigFile= open(path + "\\"+name,'w',encoding='utf-8')
        bigFile.seek(size)
        bigFile.write('\n')
        bigFile.close()
        return name

print("======================")
print("文件批量生成工具")
print("Beta1.0.0")
print("作者:ZhaoM")
print("GitHub主页:https://github.com/buke18/egao")
print("======================")
print("Beta1.0.0更新日志：")
print("1.暂无")
print("======================")
print("请进行必要的配置：")
print("======================")

mod=int(input('请选择生成文件拓展名\n1为无拓展名，2为txt，3为xls，4为doc，5为dll，6为exe，7为自定义\n'))
if(mod==1):
        suffix = ""
elif(mod==2):
        suffix = '.txt'
elif(mod==3):
        suffix = '.xls'
elif(mod==4):
        suffix = '.doc'
elif(mod==5):
        suffix = '.dll'
elif(mod==6):
        suffix = '.exe'
elif(mod==7):
        suffix = input('生成文件拓展名（需带.）\n')
else:
        print("suffix mod error")
        suffix = ""
print("======================")

mod=int(input('请选择生成文件位置\n1为当前目录，2为根目录，3为自定义目录\n'))
if(mod==1):
        path = ""
elif(mod==2):
        path = 'C:'
elif(mod==3):
        path = input('生成文件路径（后面无需带\）\n')
else:
        print("path mod error")
        path = ""
print("======================")
        
mod=int(input('请选择生成文件单位\n1为KB，2为MB，3为GB，4为自定义区间随机大小\n'))
if(mod==1):
        isrand=1
        print("======================")
        size = int(input('文件大小[单位KB]\n'))
        size= int(size * 1024)
elif(mod==2):
        isrand=1
        print("======================")
        size = int(input('文件大小[单位MB]\n'))
        size= int(size * 1024 * 1024)
elif(mod==3):
        isrand=1
        print("======================")
        size = int(input('文件大小[单位GB]\n'))
        size= int(size * 1024 * 1024 * 1024)
elif(mod==4):
        print("======================")
        mod=int(input('请选择生成文件单位\n1为KB，2为MB，3为GB\n'))
        if(mod==1):
                isrand=2
                print("======================")
                minsize = int(input('最小文件大小[单位KB]\n'))
                minsize= int(minsize * 1024)
                maxsize = int(input('最大文件大小[单位KB]\n'))
                maxsize= int(maxsize * 1024)
        elif(mod==2):
                isrand=2
                print("======================")
                minsize = int(input('最小文件大小[单位MB]\n'))
                minsize= int(minsize * 1024 * 1024)
                maxsize = int(input('最大文件大小[单位MB]\n'))
                maxsize= int(maxsize * 1024 * 1024)
        elif(mod==3):
                isrand=2
                print("======================")
                minsize = int(input('最小文件大小[单位GB]\n'))
                minsize= int(minsize * 1024 * 1024 * 1024)
                maxsize = int(input('最大文件大小[单位GB]\n'))
                maxsize= int(maxsize * 1024 * 1024 * 1024)
        else:
                isrand=2
                print("size mod error")
                print("======================")
                minsize = int(input('最小文件大小[单位KB]\n'))
                minsize= int(minsize * 1024)
                maxsize = int(input('最大文件大小[单位KB]\n'))
                maxsize= int(maxsize * 1024)
                
        if(maxsize<=0):
                print("maxsize error")
                maxsize=1024
                
        if(minsize<=0):
                print("minsize error")
                minsize=1024
else:
        print("size mod error")
        print("======================")
        size = int(input('文件大小[单位KB]\n'))
        size= int(size * 1024)
if(isrand==1):
        if(size<=0):
                print("size error")
                size=1024
print("======================")

num=int(input('请输入生成数量\n'))
if(num<=0):
        print("num error")
        num=1
print("======================")

print("配置完毕！即将启动生成工具")
print("======================")
print("开始生成")
print("======================")

count = 0
while (count < num):
        count = count + 1
        print("正在生成第"+str(count)+"个文件")
        if(isrand==1):
                name=creatfile(path,size,suffix)
        else:
                size=random.uniform(minsize, maxsize)
                name=creatfile(path,size,suffix)
        print("第"+str(count)+"个文件["+name+"]生成成功")

        
print("======================")
