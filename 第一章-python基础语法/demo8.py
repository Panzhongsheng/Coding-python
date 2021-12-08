"""python文件与异常"""

'''
    文件
    1.文件读取数据
    2.文件写入数据

    注意:
    1.读取文本文件时,Python将其中的所有文本都解读为字符串。如果你读取的是数字,并
        要将其作为数值使用,就必须使用函数int()将其转换为整数,或使用函数float()将其转
        换为浮点数。
    2.打开文件时,可指定读取模式('r')、写入模式('w')、附加模式('a')或让你能够读取和写入文件的模式('r+')
'''

### 1.文件读取数据 ###
# 函数open()接受一个参数:要打开的文件的名称，默认在当前执行的文件所在的目录中查找指定的文件，也可以使用绝对路径或者相对路径
# 返回的是一个文件对象
# 使用with进行上下文管理的时候open读取文件不需要使用close进行关闭，python会自动关闭。同时也可以使用open和close进行读取文件
with open("demo8_1.txt") as fp:
    # 读取文件的所有的内容。为read()到达文件末尾时返回一个空字符串,而将这个空字符串显示出来时就是一个空行
    contents=fp.read()
    print(contents.rstrip())
with open("demo8_1.txt") as fp:
    # 每行的末尾都有一个看不见的换行符,print语句也会加上一个换行符,因此每行末尾都有两个换行符
    for line in fp:
        # 使用rstrip来消除换行符
        print(line.rstrip())
with open("demo8_1.txt") as fp:
    # readlines()从文件中读取每一行,并将其存储在一个列表中
    print(fp.readlines())
    
    
###  2.文件写入数据 ###
# 未创建的文件，open()会自动创建文件
file_name="demo8_2.txt"
# 以w模式进行写入的话，如果指定的文件已经存在,Python将在返回文件对象前清空该文件。
with open(file_name, "w") as f:
    # Python只能将字符串写入文本文件，若要使用数字则需要转换为str
    # 需要主动添加换行符
    f.write("我正在往文件写入数据\n")
    f.write(str(3.1415926))
    
'''
    异常
    1. 使用 try-except 代码块
    2. else 代码块

    注意:Python使用被称为异常的特殊对象来管理程序执行期间发生的错误.每当发生让Python不知
        所措的错误时,它都会创建一个异常对象。如果你编写了处理该异常的代码,程序将继续运行;
        如果你未对异常进行处理,程序将停止,并显示一个traceback,其中包含有关异常的报告
'''
### 1. 使用 try-except 代码块 ###
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    # Python有一个pass语句,可在代码块中使用它来让Python什么都不要做
    pass
    
### 2. else 代码块 ###
# 依赖于try代码块成功执行的代码都放在else代码块中
try:
    print(5/1)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("this is a correct statement")
    
'''
    存储数据
    1. 使用 json.dump()和 json.load()

'''
### 1. 使用 json.dump()和 json.load() ###
import json
numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
file_name='numbers.json'
with open(file_name,'w') as json_file:
    # 写入json文件
    json.dump(numbers,json_file)
    
with open(file_name,'r') as json_file:
    # 读取json文件
    print("json文件的数据为:",json.load(json_file))