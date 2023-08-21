# -*- coding: utf-8 -*-

"""
    此脚本用于搜索指定目录下的特定后缀文件。
    ——————————————————————————
    模块化文件，不单独使用！

    Last commit info:
    ~~~~~~~~~~~~~~~~~
    $LastChangedDate: 2022/03/18
    $Annotation: Create.
    $Author: xiyan19
"""


import os


def search_dir(path, result, postfix=None):
    for f in os.listdir(path):
        temp_path = os.path.join(path, f)
        if os.path.isdir(temp_path):
            search_dir(temp_path, result, postfix)
        else:
            if postfix is not None:
                if temp_path.split('.')[-1] == postfix:
                    result.append(temp_path)
            else:
                result.append(temp_path)

    return result
