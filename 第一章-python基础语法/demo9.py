"""python测试代码：编写函数或类时,还可为其编写测试"""

'''
    测试函数
    1.自己编写测试函数
    2.unittest代码测试工具
    
    拓展:
    1.单元测试用于核实函数的某个方面没有问题; 
        测试用例是一组单元测试,这些单元测试一起核实函数在各种情形下的行为都符合要求。
    2.最初只要针对代码的重要行为编写测试即可,等项目被广泛使用时再考虑全覆盖
    3.测试未通过时,不要修改测试,而应修复导致测试不能通过的代码:检查刚对函数所做的修改,找出导致函数行为不符合预期的修改。
    4.assertEqual(a, b)     核实a == b
      assertNotEqual(a, b)  核实a != b
      assertTrue(x)         核实x为True
      assertFalse(x)        核实x为False
      assertIn(item, list)  核实item 在list中
      assertNotIn( item , list)  核实item 不在list中
 

'''
def getFormattedName(first_name,last_name):
    full_name = first_name+last_name
    return full_name.title()

### 1.自己编写测试函数 ###
def testGetFormattedName():
    while True:
        first=input("请输入你的姓: ")
        last=input('请输入你的名: ')
        if last == 'q':
            break
        if first == 'q':
            break
        fomatted_name=getFormattedName(first,last)
        print('Test fomatted_name is: '+fomatted_name)
# testGetFormattedName()

### 2.unittest代码测试工具 ###

import unittest
# 继承unittest.TestCase的类成为一名光荣的测试类
class NameTestCase(unittest.TestCase):
    """测试getFormattedName函数"""
    # 若测试类中包含了setUp，那么它将会优先其他的方法执行。可以用于初始化测试的集合
    def setUp(self):
        """创建一个调查对象和一组答案,供使用的测试方法使用"""
        self.responses = "Janisjoplin"
    def testFirstLastName(self):
        """是否能够正确处理该姓名"""
        formatted_name = getFormattedName('janis', 'joplin')
        # 一个断言方法。断言方法用来核实得到的结果是否与期望的结果一致
        self.assertEqual(formatted_name,self.responses )
    # 凡是在测试类中的方法都会被调用
    def test(self):
        print("调用了该方法")
unittest.main()
