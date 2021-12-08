"""python函数:函数是带名字的代码块,用于完成具体的工作"""

'''
    定义函数
    1.向函数传递信息
    2.关键字传递实参
    3.函数传递列表
    4.传递任意数量的实参
    5.导入整个模块
'''
# 关键字def向Python指出了函数名
def function():
    """这个是函数的注释"""
    print("这个是函数")
# 调用
function()

### 1.向函数传递信息:参数为形参 ###
def greet(username):
    print("hello,"+username)
# 这里传递的是实参 
greet("李明")

### 2.关键字传递实参:是传递给函数的名称—值对 ###
# 注意：用默认值时,在形参列表中必须先列出没有默认值的形参,再列出有默认值的实参
def describePet(animal_type,pet_name="hello"):
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 务必准确地指定函数定义中的形参名
describePet(animal_type="dog",pet_name="Wii")
# 调用默认参数
describePet("cat")


### 3.函数传递列表:虽然向函数传递列表的副本可保留原始列表的内容,但除非有充分的理由需要传递副本,否
# 则还是应该将原始列表传递给函数,因为让函数使用现成列表可避免花时间和内存创建副本,从
# 而提高效率,在处理大型列表时尤其如此。function_name(list_name[:])###


### 4.传递任意数量的实参 ###
def makeFood(*materials):
    print(materials)
# 以元组的形式传递实参
makeFood("刀","锅","砧板")
# 如果要让函数接受不同类型的实参,必须在函数定义中将接纳任意数量实参的形参放在最后。
def makeFood(time,*materials):
    print(time+"开始准备食材"+str(materials))
makeFood("11点半","刀","锅","砧板")
# 使用任意数量的关键字实参，传递的是字典形式的参数
def makeFood(time,**materials):
    print(time+"开始准备食材"+str(materials.items()))
makeFood("11点半",cut="刀")

### 5.导入整个模块:模块是扩展名为.py的文件 ###
'''
1.导入整个模块
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

2.导入模块中的某一个函数
from pizza import make_pizza,hello_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

3.给模块或者模块的函数起小名
import pizza as p
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

4.使用星号(*)运算符可让Python导入模块中的所有函数:
可通过名称来调用每个函数,而无需使用句点表示法。然而,使用并非自己编写的
大型模块时,最好不要采用这种导入方法:如果模块中有函数的名称与你的项目中使用的名称相
同,可能导致意想不到的结果:Python可能遇到多个名称相同的函数或变量,进而覆盖函数,而不是分别导入所有的函数。
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

注意：最佳的做法是,要么只导入你需要使用的函数,要么导入整个模块并使用句点表示法。
'''