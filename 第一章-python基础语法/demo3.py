"""python元组、代码风格"""

'''
    元组
    1.定义元组
    2.修改元组
    注:相比于列表,元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变,可使用元组。
'''
### 1.定义元组 ###
# Python将不能修改的值称为不可变的,而不可变的列表被称为元组
# 元组是使用圆括号而不是使用的是方括号来标识的,使用的语法与访问列表元素时使用的语法相同
rectangle=(100,200)
print("rectangle元组的第一个元素为:",rectangle[0])


### 2.修改元组 ###
# 试图修改元组的值
# 报错
# Traceback (most recent call last):
#   File "/home/pzs/vscode_project/PythonStudy/第一章-python基础语法/demo3.py", line 14, in <module>
#     rectangle[0]=200
# TypeError: 'tuple' object does not support item assignmen
# 元组的值是不能够直接修改的
# rectangle[0]=200

# 修改元组的变量值：虽然不能修改元组的元素,但可以给存储元组的变量赋值
# 
dimensions=(200,50)
print("修改元组的变量之前的值为:")
for dimension in dimensions:
    print(dimension)
dimensions=(100,20)
print("修改元组的变量之后的值为:")
for dimension in dimensions:
    print(dimension)



'''
    python代码风格
    1.格式设置指南。遵循PEP8
    2.缩进。PEP 8建议每级缩进都使用四个空格.在字处理文档中,大家常常使用制表符而不是空格来缩进。对于字处理文档来说,这样做的
        效果很好,但混合使用制表符和空格会让Python解释器感到迷惑。每款文本编辑器都提供了一种
        设置,可将输入的制表符转换为指定数量的空格。你在编写代码时应该使用制表符键,但一定要
        对编辑器进行设置,使其在文档中插入空格而不是制表符。
    3.行长。很多Python程序员都建议每行不超过80字符。PEP 8还建议注释的行长都不超过72字符
    4.空行。要将程序的不同部分分开,可使用空行。你应该使用空行来组织程序文件。空行不会影响代码的运行,但会影响代码的可读性。Python解释器根据水平缩进情况来解读
        代码,但不关心垂直间距。

'''


