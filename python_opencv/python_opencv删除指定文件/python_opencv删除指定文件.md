## python opencv删除指定文件

#### 1.运行步骤

```python
#########第一步:修改remove_file.py的directory和delete_file############

# 修改为要删除的文件夹的名称
directory = r'D:\Pycharm\PyQt5\OptoelectronicsCompetition\PictureProcessing\FileOpteration'
# 修改为要删除的文件的名称
delete_file = 'delete.txt'

#########第二步:切换到remove_file.py所在的文件夹下并运行remove_file.py############
python3 remove_file.py
```



#### 2.重要代码以及函数讲解

- ##### is_exists=os.path.exists(path)

  参数：

  - path:Text类型的字符串Text = str可以是文件夹也可以是文件，可以是相对路径也可以是绝对路径

  返回值:

  - is_exists:bool类型

  源代码解析:

  ```python
  # 要删除文件的时候首先要判断一下目录是否存在，否则在没有文件或者目录存在的情况下进行删除会报异常:FileNotFoundError
  if not os.path.exists(directory):
      print("文件夹不存在")
      return False
  ```

  python源码解析：

  ```python
  返回值:
  	1.bool类是int类的子类,但是不能够实例化子类，也就是说bool类没有子类。bool类可以强制转换为int类，而int类也可以向下转型为bool类
  print(bool(10))
  print(int(True))
  
  #结果:
  True
  1
  
  参数：
  	1.Text类型在Python 2中为unicode编码,Python 3为str
  	2.path的类型
  ```

- ##### file_list = os.listdir(directory)

  参数:

  - directory:文件夹的路径，可以为str、bytes或类似路径的对象。

  返回值:

  - file_list：返回包含目录中文件名的列表

  源代码解析:

  ```python
  # 要删除指定的文件时，首先要对准备要删除的文件的目录进行一个遍历，得到所有的文件，以便寻找要删除的文件
  file_list = os.listdir(directory)
  ```

  python源码解析：

  ```python
  参数：
   directory类型：
      1.路径可以指定为str、bytes或类似路径的对象。如果路径是字节，返回的文件名也将是字节.在所有其他情况下返回的文件名将是str。
  	2.如果directory为None，也就是directory不存在的话，则使用directory='.'。在某些平台上，路径也可以指定为打开的文件描述符\，文件描述符必须引用目录。如果此功能不可用，使用它将引发NotImplementedError。同时列表的顺序是任意的，不包括"."目录和".."目录
  ```

- ##### python的in函数

  - 使用范围:用于判断（查找）元素是否在可迭代对象中(不包括生成器,但是包括set)，常用的是**string, list, dict, tuple, generator, range**
  - 效率对比：**dict, set**背后原理是一个散列表(把关键码值映射到表中一个位置来访问记录，以加快查找的速度，简称键值对匹配)，所以使用in的时候效率高，而**tuple, list**只是一个单纯类似与数组的结构

  源代码解析:

  ```python
  # 要删除目录中的指定文件的时候要通过in来查找文件是否存在于文件夹下
  if delete_file in file_list:
  ```
  
  

- ##### os.remove(del_file)

  参数:

  - del_file:要删除的文件路径

  返回值:

  - None

  源代码解析:

  ```python
  # 删除指定的文件
  os.remove(del_file)
  ```

  python源码解析：

  ```python
  参数：
      如果del_file不是None，则它应该是打开到某个目录的文件描述符，路径应该是相对的；然后，路径将相对于该目录。del_file可能无法使用，如果不可用，使用它将引发NotImplementedError。说人话就是路径可以是相对路径也可以是绝对路径，但是必须要存在
  ```



#### 3.源码

​	remove_file.py 
