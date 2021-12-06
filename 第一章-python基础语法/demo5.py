"""python控制语句、循环语句"""

'''
    控制语句
    1.if语句
    2.input()
    3.while循环语句
'''

### 1.if语句 ###
# 每条if语句的核心都是一个值为True或False的表达式,这种表达式被称为条件测试。在Python中检查是否相等时区分大小写,
print('bwm'=='Bwm')

# 检查是否不相等：使用不等号!
hello="hello world"
if hello != "hello python":
    print("not equal")

# 使用and检查多个条件要检查是否两个条件都为 True,可使用关键字 and将两个条件测试合而为一
age=20
if age>=18 and age<=60:
    print("青年人")
# 关键字or也能够让你检查多个条件,但只要至少有一个条件满足,就能通过整个测试。仅当两个测试都没有通过时,使用 or的表达式才为False。
if age<=18 or age>=60:
    print("老幼群体")

# if-else结构非常适合用于要让Python执行两种操作之一的情形。
# Python只执行if-elif-else结构中的一个代码块,它依次检查每个条件测试,直到遇到通过了的条件测试。测试通过后,Python将执行紧跟在它后面的代码,并跳过余下的测试。
if age<4:
    print("young boy")
elif age<18:
    print("big boy")
else:
    print("boy")

### 2.input() ###
# input()让程序暂停运行,接受一个参数:指定清晰而易于明白的提示即要向用户显示的提示或说明
# 通过在提示末尾(这里是冒号后面)包含一个空格,可将提示与用户输入分开,让用户清楚地知道其输入始于何处,

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

### 3.while循环语句 ###
# 每个while循环都必须有停止运行的途径,这样才不会没完没了地执行下去。如果程序陷入无限循环,可按Ctrl + C,也可关闭显示程序输出的终端窗口。

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    # 控制退出的时机
    if current_number == 3:
        break




