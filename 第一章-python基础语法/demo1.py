'''Python变量、字符串、数字、注释'''

"""
    python变量赋值
"""
# python通过赋值语句"="将值赋值给变量,每个变量都存储了一个值——与变量相关联的信息
message="hello,world"
print(message)
# Python将始终记录变量的最新值
message="change the value"
print(message)

"""
    python变量命名规范:
    1.变量名只能包含字母、数字和下划线
    2.变量名不能包含空格,但可使用下划线来分隔其中的单词
    3.不要将Python关键字和函数名用作变量名
    4.变量名应既简短又具有描述性
    5.慎用小写字母l和大写字母O,因为它们可能被人错看成数字1和0。

    错误命名:1_message、greeting message、print 
    不规范命名:a、l
    规范命名:推荐用小写字母命名变量:user_name
"""

"""
    python错误
    python是解释型语言，从上往下运行,当程序无法成功地运行时,解释器会提供一个traceback。traceback是一条记录,指出了解释器尝试运行代码时,在什么地方陷入了困境。     
    Traceback (most recent call last):  
        File "/home/pzs/vscode_project/PythonStudy/第一章/demo1.py", line 28, in <module>   （1）
           print(mesage)     （2）
    NameError: name 'mesage' is not defined  （3）
    
    (1):错误的位置 (2):错误的语句  (3):错误类型
    
    错误类型:
    名称错误通常意味着两种情况:要么是使用变量前忘记了给它赋值,要么是输入变量名时拼写不正确。
    类型错误通常意味着函数操作的数据的类型不匹配
"""
message="test traceback"
# print(mesage) # 名称错误


"""
    python字符串
    1.字符串就是一系列字符。在Python中,用引号括起的都是字符串,其中的引号可以是单引号,也可以是双引号
    2.字符串函数:对字符串进行一系列的处理
         title()
         upper()
         lower()
         +
         strip()
         rstrip()
         lstrip()
         
"""
# 可以在单引号中包括双引号，在双引号中包含单引号
string1='I told my friend, "Python is my favorite language!"'
string2="The language 'Python' is named after Monty Python, not the snake."
# 使用转义字符可以在双引号中加双引号(转义字符:在双引号前面加个转义符 \ ，即反斜杠)
string3="One of \"Python's strengths\" is its diverse and supportive community."
# 类C语言的printf可以进行格式化输出
print("string1:%s\nstring2:%s\nstring:%s" %(string1,string2,string3))

# title()函数将字符串的首字母大写，其余不变。每个方法后面都跟着一对括号（因为方法通常需要额外的信息来完成其工作）
title_func_string="ada local"
print(title_func_string.title())
upper_func_string="Ada local"
# upper():字母全部大写
print(upper_func_string.upper())
#lower(): 字母全部小写
print(upper_func_string.lower())
# +:字符串拼接
print(title_func_string+upper_func_string)
# strip：删除空白
strip_func_string=" python "
# 去除右边
print(strip_func_string.rstrip())
# 去除左边
print(strip_func_string.lstrip())
# 去除两边
print(strip_func_string.strip())


"""
    python数字
    1.整数    
    2.浮点数：Python将带小数点的数字都称为浮点数，通常结果包含的小数位数可能是不确定的
    3.可调用函数str(),它让Python将非字符串值表示为字符串
"""
print(2+3)
print(3-2)
print(2*3)
# 3的2次方
print(3**2)
#3除2，为小数
print(3/2)
# 向下取整的除法
print(3//2)
# 小数位数可能是不确定的,可以经过一些处理得到想要的具体的位数
print( 3 * 0.1)

# str()，不能直接用整数和字符串进行字符串的拼接，会报类型错误
str_int=str(123)
message="happy"+str_int
print(message)


"""
    pytho注释
    1.#：在Python中,注释用井号( #)标识。井号后面的内容都会被Python解释器忽略
    2.'''多行注释内容''':python的多行注释

    注释编写的注意事项:
    1.以清晰的自然语言对解决方案进行概述,可节省很多时间。
    2.要成为专业程序员或与其他程序员合作,就必须编写有意义的描述性注释
    3.最值得养成的习惯之一是,在代码中编写清晰、简洁的注释。
    4.找到合理的解决方案前,是否考虑了多个解决方案。如果答案是肯定的,就编写注释对你的解决方案进行说明吧。
    5.现实是复杂的,有时候可能没有简单的解决方案。在这种情况下,就选择最简单可行的解决方案吧。
    6.即便是复杂的代码,也要让它易于理解。
    7.先编写行之有效的代码,再决定是对其做进一步改进,还是转而去编写新代码。

"""