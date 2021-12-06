'''python列表'''

"""
    python列表
    1.列表由一系列按特定顺序排列的元素组成
    2.在Python中,用方括号([])来表示列表,并用逗号来分隔其中的元素。
    3.给列表指定一个表示复数的名称(如letters、digits或names )是个不错的主意。
    4.列表内元素可以为不同类型，如字符串和整数组合的列表
    5.列表都将是动态的,列表创建后,将随着程序的运行增删元素.
    6.创建列表的一种方法:首先创建一个空列表,用于存储用户将要输入的值,然后将用户提供的每个新值附加到列表中。
    7.列表有许多内置的方法，如append、insert、del、pop、remove、sort、sorted、len
    8.列表使用时候要特别注意索引的错误.发生索引错误却找不到解决办法时,请尝试将列表或其长度打印出来

"""
names = ['panzhongsheng', 18, 'peter', 20]
print("列表为:",names)

# 访问列表元素,指定元素的索引(从0开始)
print("0号元素为:",names[0])

# 通过将索引指定为-1,可让Python返回最后一个列表元素
# 索引-2返回倒数第二个列表元素,索引-3返回倒数第三个列表元素,以此类推
print("最后一位元素为:",names[-1])

names[0]="God"
print("0号位置赋值为God后:",names)

# append将元素附加到列表末尾
names.append("Tom")
print("列表末尾追加Tom后:",names)

# 指定索引插入元素
names.insert(0,"Cat")
print("0号位置插入Cat元素后:",names)

# 删除指定索引的元素，使用del可删除任何位置处的列表元素,条件是知道其索引。
del names[0]
print("删除0号元素后names为:",names)

# pop()将列表的最后一个元素弹出,并且返回最后的一个元素
poped_name=names.pop()
print("列表的最后一个值为:",poped_name)
print("弹出最后一个元素后names为::",names)

# 以使用 pop()来删除列表中任何位置的元素,只需在括号中指定要删除的元素
# 的索引即可。
specific_poped_name=names.pop(1)
print("弹出指定的列表元素:%d" % specific_poped_name)

# 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次,就需要使用循环来判断是否删除了所有这样的值。
remove_name="peter"
names.remove(remove_name)
print("删除peter后列表为:",names)

# sort()为就地操作，直接对原来的列表进行操作
# 排序的原则是:按照字母的顺序或者数字的大小来进行
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print("排序后cars为:",cars)
cars.sort(reverse=True)
print("反向排序后cars为:",cars)

# 要保留列表元素原来的排列顺序,同时以特定的顺序呈现它们,可使用函数sorted()
print("排序后的新列表为:",sorted(cars))
print("反向排序后的新列表为:",sorted(cars,reverse=True))
print("原列表cars为:",cars)

# 方法reverse() 永久性地修改列表元素的排列顺序,但可随时恢复到原来的排列顺序,为此只需对列表再次调用reverse()即可。
cars.reverse()
print("反向排序后的cars为:",cars)

# 获取列表长度:推荐使用，python内置方法速度快
print("cars的列表长度为:",len(cars))

# print(cars[7])  #IndexError: list index out of range


'''
    列表操作
    1.对列表中的每个元素,都将执行循环指定的步骤,而不管列表包含多少个元素。如果列表包含一百万个元素,Python就重复执行指定的步骤一百万次,且通常速度非常快。
    2.列表元素和列表命名:使用单数和复数式名称,可帮助你判断代码段处理的是单个列表元素还是整个列表
    3.Python通过使用缩进让代码更易读;简单地说,它要求你使用缩进让代码整洁而结构清晰。缩进一般为4个空格
    4.创建数值列表
    5.列表推导式子。
    6.切片 
    7.复制列表
    8.检查列表元素
 
'''
cars=["奔驰","宝马","拖拉机"]
for car in cars:
    # 可以对列表元素进行相关的操作
    print(car.title())
print("for循环结束后的操作")

# Python函数 range() 让你能够轻松地生成一系列的数字
# 区间为左闭右开
for value in range(1,5):
    print(value)
# 创建数字列表,将range()转换为list
numbers=list(range(1,5))
print("numbers数字列表为:",numbers)

# 指定步长的range(start_position,end_position,step)
odd_numbers=list(range(2,10,2))
print("odd_numbers列表中偶数数字为:",odd_numbers)

# 列表的相关操作函数
digits=[1,2,3,4,5,6,7,8,9]
print("digits列表的最小值为:",min(digits))
print("digits列表的最大值为:",max(digits))
print("digits列表之和为:",sum(digits))

# 列表推导式：将for循环和创建新元素的代码合并成一行,并自动附加新元素
squares=[radius**2 for radius in range(1,11)]
print("squares列表为:",squares)
# 列表推导式等价for循环形式
squares=[]
for radius in range(1,11):
    squares.append(radius**2)
print("squares列表为:",squares)

### 6.切片 ###
# [start_position:end_positon]:可以为正数或者负数，只要符合逻辑
animals=['cat','mouse','dog','eagle']
print("animals列表前三个值为:",animals[0:3])
# 如果你没有指定第一个索引,Python将自动从列表开头开始:
print("animals列表为:",animals[:])
# 从倒数第三个到最后一个列表元素
print(animals[-3:])

### 7.复制列表 ###
# 副本复制:可创建一个包含整个列表的切片,方法是同时省略起始索引和终止索引([:])。
my_foods=["汉堡包","薯条","炸鸡"]
my_friends_foods=my_foods[:]
print("我点的食物为:",my_foods)
print("我朋友点的食物为:",my_friends_foods)
my_friends_foods[0]="可乐"
print("我朋友口渴了，想把汉堡包换成可乐，所有他最终的食物为:",my_friends_foods)

# 引用复制:直接将列表复制给其他的列表对象.对任何一个列表进行操作的时候都会影响到另外一个列表的值，原则上这个两个列表是同一个列表
# 相当于我和我的朋友共享一份食物
my_friends_foods=my_foods
my_foods.append("鸡腿")
print("我和我朋友一起吃的食物为:",my_friends_foods)


### 8.检查列表元素 ###
# 使用in操作符可以有效地检查列表内是否存在某个元素
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print( 'mushrooms' in requested_toppings)

# 查特定值是否不包含在列表中.在这种情况下,可使用关键字not in。
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print("Sorry you are not in the banned_users")

# 在对列表操作的时候判断是否为空很重要
if len(requested_toppings) == 0:
    print("empty list")
else:
    print("do some operation about the list")