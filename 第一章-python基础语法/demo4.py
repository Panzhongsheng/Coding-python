'''python字典'''

"""
    字典
    1.使用字典    
    2.遍历字典
"""

###  1.使用字典 ### 
# 在Python中,字典是一系列键—值对。每个键都与一个值相关联,你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上,可将任何Python对象用作字典中的值。
colors={'red':0,'green':1,'blue':2}
# 访问字典的值
print("red的值为:",colors['red'])
# 添加键值对:字典是一种动态结构,可随时在其中添加键—值对。要添加键—值对,可依次指定字典名、用方括号括起的键和相关联的值
#  Python不关心键—值对的添加顺序,而只关心键和值之间的关联关系。
colors['yellow'] =3
print("添加Yellow后的colors字典为:",colors)

# 空键值对
empty_dict={}
print("空键值对:",empty_dict)

# 修改键值对的值
colors['yellow']=10
print("修改后的colors字典为:",colors)

# 删除键值对
del colors["yellow"]
print("删除yellow后的colors字典为:",colors)

###  2.遍历字典 ### 
# items():返回一个键—值对列表,即便遍历字典时,键—值对的返回顺序也与存储顺序不同。
person={"name":"Tom",'age':18,"id":18}
for key,value in person.items():
    print("key:",key)
    print("value:",value) 
# 方法keys()并非只能用于遍历;实际上,它返回一个列表,其中包含字典中的所有键
for key in person.keys():
    print("get the key:",key)
# 对key进行一个排序
for sorted_key in sorted(person.keys()):
    print("sorted the key is:",sorted_key)
# 它返回一个值列表,而不包含任何键
for value in person.values():
    print("get the value:",value)
# 为剔除重复项,可使用集合(set)。集合类似于列表,但每个元素都必须是独一无二的
for set_value in set(person.values()):
    print("set value is:",set_value)