"""python类：根据类来创建对象被称为实例化"""


'''
    创建和使用类
    1.定义类
    2.python标志库类
    3.类编码风格
'''

# 父类必须包含在当前文件中,且位于子类前面。。父类也称为超类(superclass)
class Animals():
    def __init__(self,name):
        print("我是动物类的父类,动物的名字为:",name)


# 在Python中,首字母大写的名称指的是类
# 一个类继承另一个类时,它将自动获得另一个类的所有属性和方法;原有的类称为父类,而新类称为子类
class Dog(Animals):
    """类的文档注释"""
    # 类的初始化函数，可以定义类的初始化成员变量.每当你根据Dog类创建新实例时,Python都会自动运行它
    # 当你使用了默认参数指定属性的默认值的时候就无需提供类的形参
    def __init__(self,name="pekky",age=1):
        # 初始化父类的属性
        super().__init__(name)
        # 属性
        self.name = name
        self.age = age
        print("创建实例自动初始化")
    # python类中函数形参self必不可少,与类相关联的方法调用都自动传递实参self
    # 它是一个指向实例本身的引用,让实例能够访问类中的属性和方法。
    def eat(self):
        print("狗啃骨头")
    # 类的函数叫做类的方法
    def sitDown(self):
        """函数注释"""
        print("狗原地坐下")
    def modifyName(self,name):
        self.name = name
    
###  2.python标志库类 ###
# OrderedDict:它兼具列表和字典的主要优点(在将信息关联起来的同时保留原来的顺序)
from collections import OrderedDict
favorite_languages=OrderedDict()
favorite_languages['peter']="java"
favorite_languages['kite']="python"
for name,language in favorite_languages.items():
    print("name is:{0},favorite_language is {1}".format(name,language))
    

###  3.类编码风格 ###
'''
    1.类名应采用驼峰命名法,即将类名中的每个单词的首字母都大写,而不使用下划线
    2.对于每个类,都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的
      功能,并遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文档字符串,
      对其中的类可用于做什么进行描述。
    3.在类中,可使用一个空行来分隔方法;而在模块中,可使用两个空行来分隔类。
    4.先编写导入标准库模块的import语句,再添加一个空行,然后编写导入你自己编写的模块的import语句
'''


# python的main函数
if __name__ == '__main__':
    # 创建类的实例对象
    dog1=Dog("pekky",18)    
    # 访问属性要访问实例的属性或者方法,可使用句点表示法
    print(dog1.name)
    dog1.eat()
    # 当你使用了默认参数指定属性的默认值的时候就无需提供类的形参
    dog2=Dog()
    dog2.name="kitty"
    print("直接修改实例对象的属性:",dog2.name)
    dog2.modifyName("petty")
    print("通过方法来间接修改实例对象的属性:",dog2.name)