import os

"""python opencv删除指定文件夹下的文件"""


def removeFile(directory, delete_file):
    """
    python删除指定文件夹下，指定字符串文件
    :param delete_file:删除的
    :param directory:
    :return:
    """
    # 要删除文件的时候首先要判断一下目录是否存在
    # 否则在没有文件或者目录存在的情况下进行删除会报异常:FileNotFoundError
    if not os.path.exists(directory):
        print("文件夹不存在")
        return False
    # 要删除指定的文件时，首先要对准备要删除的文件的目录进行一个遍历，得到所有的文件，
    # 以便寻找要删除的文件
    file_list = os.listdir(directory)
    # 要删除目录中的指定文件的时候要通过in来查找文件是否存在于文件夹下
    if delete_file in file_list:
        # os.remove(path),path 表示目标文件所在的路径，可以使用相对路径或者绝对路径
        # 当文件不存在的时候会报异常:FileNotFoundError
        os.remove(delete_file)
        print("删除文件成功")
        return True
    else:
        print("文件不存在")
        return False


if __name__ == '__main__':
    # 要删除的文件的名称
    directory = r'D:\Pycharm\PyQt5\OptoelectronicsCompetition\PictureProcessing\FileOpteration'
    # 要删除的文件的名称
    delete_file = 'delete.txt'
    is_delete = removeFile(directory, delete_file)
    if is_delete:
        print("已经删除文件")
    else:
        print("删除文件失败")
