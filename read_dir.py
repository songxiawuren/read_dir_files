"""
非递归读取某文件夹及其子文件夹下所有文件
"""
import os
import sys

def read_files_in_dir(path_list):
    """读取某个文件夹及其子文件夹下所有文件"""
    file_list = []
    dir_list = path_list
    absolute_path_list = path_list
    loop = True
    while loop:
        for sub_path in absolute_path_list:
            if not os.path.isdir(sub_path):
                dir_list.remove(sub_path)
                continue
            relative_path_list = os.listdir(sub_path)
            dir_list.remove(sub_path)  #遍历当前文件夹下的子目录时，需要把当前目录移除，因为其已被处理过
            absolute_path_list = make_absolute_path(sub_path, relative_path_list)
            for path_name in absolute_path_list:
                if os.path.isdir(path_name):
                    dir_list.append(path_name)
                else:
                    file_list.append(path_name)
        absolute_path_list = dir_list
        if not dir_list:
            loop = False
    return file_list

def make_absolute_path(base_path, relative_path_list):
    """把当前文件夹下的目录或文件转成绝对路径"""
    absolute_path_list = []
    for name in relative_path_list:
        absolute_path_list.append(base_path + '/' + name)
    return absolute_path_list

def print_file_list(file_list):
    """控制台输出"""
    for file in file_list:
        print(file)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("需要至少两个参数才能运行")
        exit(1)
    paths_list = []
    for _, arg in enumerate(sys.argv, 1):
        paths_list.append(arg)
    print_file_list(read_files_in_dir(paths_list))
    