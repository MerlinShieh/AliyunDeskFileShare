# -*- coding: utf-8 -*-

import os


def get_files_type(_file_name: str) -> str:
    """
    获取文件后缀名
    :param _file_name: 文件路径/名称
    :return: 后缀名 .jpg
    """
    return os.path.splitext(_file_name)[1]


def add_type(_file_name: str, _type: str):
    """
    增加文件类型关键字至二进制文件最后面
    """
    with open(_file_name, 'ba+') as f:
        f.seek(0, 2)
        f.write(('\n' + _type).encode())


def del_type(_file_name: str):
    """
    删除二进制文件最后面的.jpg这种描述
    """
    with open(_file_name, "rb") as f:
        f_list = f.readlines()
        f.close()
    with open(_file_name, 'wb') as f:
        f_list.pop()
        for i in f_list:
            f.write(i)
        f.seek(-1, 2)
        f.truncate()


def replace_type(_file_name: str) -> str:
    """
    更改名称，主要是更改后缀名
    """
    if get_files_type(_file_name) != '.txt':
        old_name = _file_name
        new_name = _file_name.replace(get_files_type(_file_name), '.txt')
        os.rename(old_name, new_name)
        return new_name
    if get_files_type(_file_name) == '.txt':
        with open(_file_name, 'rb') as f:
            lines = f.readlines()  # 读取所有行
            _rel_type = lines[-1].decode('utf-8')  # 取最后一行

        if _rel_type[0] == '.':
            old_name = _file_name
            new_name = _file_name.replace(get_files_type(_file_name), _rel_type)
            os.rename(old_name, new_name)
            return new_name
        else:
            return 'False'


if __name__ == '__main__':
    file_name = input('请输入文件名称（路径）:')
    if get_files_type(file_name) == '.txt':
        file_name = replace_type(file_name)
        if file_name:
            del_type(file_name)
            print('Success -----> ', file_name)
        else:
            print(file_name)
    else:
        add_type(file_name, get_files_type(file_name))
        file_name = replace_type(file_name)
        print('Success -----> ', file_name)
