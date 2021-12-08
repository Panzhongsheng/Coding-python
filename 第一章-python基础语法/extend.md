### 附录 

#### 1.寻求帮助

```markdown
第一步：陷入困境后,首先需要判断形势。你必须能够明确地回答如下三个问题：
1）你想要做什么?（描述的问题要具体并且详细） e.g.我要在我的Windows 10计算机上安装最新版本的Python 3

2）你已尝试哪些方式?（答案应该提供足够多的细节,这样别人就不会建议你去重复已经尝试过的方式） e.g.,我访问http://python.org/downloads/,并单击Python 3的Download按钮,再运行这个安装程序

3）结果如何?(知道准确的错误消息对在线搜索解决方案或寻求帮助很有用)

第二步：再试试
只需回过头去重新来一次,就足以解决很多问题。

第三步：歇一会儿
如果你很长时间内一直在试图解决同一个问题,那么休息一会儿实际上是你可采取的最佳战
术。长时间从事一个任务时,你可能变得一根筋,脑子里想的都是一个解决方案。你对所做的假
设往往会视而不见,而休息一会儿有助于你从不同的角度看问题。


第四步：在线搜索
1） 例如,如果你无法在使用Windows 10的计算机上安装Python 3,那么搜索“python 3 windows 10”可能会让你马上找到解决问题的方案。
2） 例如,假设你试图启动Python终端会话时出现了如下错误消息:
> python
'python' is not recognized as an internal or external command
>
通过搜索完整的错误消息“python is not recognized as an internal or external command ”,也许能得到不错的建议。
3）如果文章没有任何评论,请对其持保留态度——它提供的建议可能还没有人验证过。
```


#### 2. Git版本控制

- 在 Linux 系统中安装 Git

  ```sh
  $ sudo apt-get install git
  ```

- 查看git的版本,若显示成功后就为成功安装好git

  ```sh
  pzs@pzs-Lenovo-Legion-R7000-2020:~$ git --version 
  git version 2.25.1
  ```

- 配置 Git
  Git跟踪谁修改了项目,哪怕参与项目开发的人只有一个。为此,Git需要知道你的用户名和电子邮件地址。你必须提供用户名,但可以使用虚构的电子邮件地址:

  ```sh
  $ git config --global user.name "username"
  $ git config --global user.email "username@example.com"
  ```

- 忽略文件
  扩展名为.pyc的文件是根据.py文件自动生成的,因此我们无需让Git跟踪它们。这些文件存储在目录__pycache__中。为让Git忽略这个目录,创建一个名为.gitignore的特殊文件(这个文件名以句点打头,且没有扩展名),并在其中添加下面一行内容:

  ```markdown
  __pycache__/
  ```

  这让Git忽略目录__pycache__中的所有文件。使用文件.gitignore可避免项目混乱,开发起来更容易。

- 初始化仓库
  你创建了一个目录,其中包含一个Python文件和一个.gitignore文件,可以初始化一个Git仓库了。

  ```shell
  git_practice$ git init
  Initialized empty Git repository in git_practice/.git/
  ```

  注意:。仓库是程序中被Git主动跟踪的一组文件。Git用来管理仓库的文件都存储在隐藏的.git/中,你根本不需要与这个目录打交道,但千万不要删除这个目录,否则将丢弃项目的所有历史记录。

- 检查状态：执行其他操作前,先来看一下项目的状态

  ```sh
  pzs@pzs-Lenovo-Legion-R7000-2020:~/vscode_project/PythonStudy/第一章-python基础语法$ git status
  On branch master
  
  No commits yet
  
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
  	.gitignore
  	demo1.py
  	demo2.py
  	demo3.py
  	demo4.py
  	demo5.py
  	demo6.py
  	demo7.py
  	demo8.py
  	demo8_1.txt
  	demo8_2.txt
  	demo9.py
  	extend.md
  	numbers.json
  
  nothing added to commit but untracked files present (use "git add" to track)
  
  注意:在Git中,分支是项目的一个版本。从这里的输出可知,我们位于分支master上
  ```

- 将文件加入到仓库中

  ```sh
   pzs@pzs-Lenovo-Legion-R7000-2020: git add . 
  ```

  ​	注意:命令git add .将项目中未被跟踪的所有文件都加入到仓库中(见)。它不提交这些文件,而只是让Git开始关注它们

- 执行提交

  ```sh
  pzs@pzs-Lenovo-Legion-R7000-2020:~/vscode_project/PythonStudy/第一章-python基础语法$ git commit -m "Started project"
  [master (root-commit) 6213dbd] Started project
   14 files changed, 855 insertions(+)
   create mode 100644 .gitignore
   create mode 100644 demo1.py
   create mode 100644 demo2.py
   create mode 100644 demo3.py
   create mode 100644 demo4.py
   create mode 100644 demo5.py
   create mode 100644 demo6.py
   create mode 100644 demo7.py
   create mode 100644 demo8.py
   create mode 100644 demo8_1.txt
   create mode 100644 demo8_2.txt
   create mode 100644 demo9.py
   create mode 100644 extend.md
   create mode 100644 numbers.json
  ```

  注意:执行命令git commit -m "message"(见)以拍摄项目的快照。标志-m让Git将接下来的消息("Started project.")记录到项目的历史记录中。输出表明我们在分支master上

-  查看提交历史

  ```sh
  pzs@pzs-Lenovo-Legion-R7000-2020:~/vscode_project/PythonStudy/第一章-python基础语法$ git log
  commit 6213dbd5014a0ee6bc7122d31b70ccee9533d41f (HEAD -> master)
  Author: Panzhongsheng <2647672511@qq.com>
  Date:   Thu Dec 9 01:18:43 2021 +0800
  
      Started project
  ```

  注意：,Git都会生成一个包含40字符的独一无二的引用ID。它记录提交是谁执行的、
  提交的时间以及提交时指定的消息。并非在任何情况下你都需要所有这些信息,因此Git提供了一个选项,让你能够打印提交历史条目的更简单的版本

  ```sh
  pzs@pzs-Lenovo-Legion-R7000-2020:~/vscode_project/PythonStudy/第一章-python基础语法$ git log --pretty=oneline 
  6213dbd5014a0ee6bc7122d31b70ccee9533d41f (HEAD -> master) Started project
  ```

  

- 第二次提交

  ```sh
   git_practice$ git commit -am "Extended greeting."
   [master 08d4d5e] Extended greeting.
  1 file changed, 1 insertion(+) 
  ```

  注意：我们再次执行了提交,并在执行命令git commit时指定了标志-am(见)。标志-a让Git将仓库中所有修改了的文件都加入到当前提交中(如果你在两次提交之间创建了新文件,可再次执行命令git add .将这些新文件加入到仓库中)。标志-m让Git在提交历史中记录一条消息。

- 恢复到以前的操作

  ```sh
  git_practice$ git checkout .
  git_practice$ git status
  # On branch master
  nothing to commit, working directory clean
  ```

  注意：命令git checkout让你能够恢复到以前的任何提交。命令git checkout .放弃自最后一次提交后所做的所有修改,将项目恢复到最后一次提交的状态。

-  删除仓库

  如果无法恢复且参与项目开发的只有你一个人,可继续使用这些文件,但要将项目的历史记录删除——删除目录.git。这不会影响任何文件的当前状态,而只会删除所有的提交,因此你将无法检出项目的其他任何状态。