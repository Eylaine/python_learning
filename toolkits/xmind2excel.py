# -*- coding: utf-8 -*-
# @Time    : 2019-08-05 16:21
# @Author  : Eylaine
# @File    : xmind2excel.py

import sys
import xmind
import time
from openpyxl import load_workbook
import shutil
from os.path import splitext
import os

"""xmind to excel for teambition"""

_PATH = os.path.dirname(os.path.abspath(__file__))

template_name = "template.xlsx"

path_list = list()

_author = "admin"

log_file = "log.txt"


def read_xmind(file_path):
    """
    读取xmind文件内容
    :param file_path:
    :return:
    """
    work_book = xmind.load(file_path)
    sheet = work_book.getSheets()[0]
    sheet_name = sheet.getTitle()
    root_topic = sheet.getRootTopic()

    path = sheet_name
    get_leaf_path(root_topic, path)

    case_list = list()

    for case in path_list:

        step_list = case.split("#")

        level = get_level(step_list[-1])
        if level == "":
            """优先级没写"""
            print("缺少优先级：" + str(step_list))
            with open(log_file, 'a+') as log:
                log.write("缺少优先级：" + str(step_list) + "\n")
            assert False

        step_index = get_step_index(step_list)
        if step_index == 0:
            """Step没写"""
            print("缺少Step标示：" + str(step_list))
            with open(log_file, 'a+') as log:
                log.write("缺少Step标示：" + str(step_list) + "\n")
            assert False
        # 有Step表示的节点至倒数第二个为测试步骤
        steps = get_step(step_list[step_index:-1])
        # 根节点的第一级子节点到Step前一个节点为标题
        title = get_title(step_list[2:step_index])
        # Sheet名称 + 根节点 + 根节点第一级子节点为分组
        group = get_group(step_list[0:4])
        # 最后一个为预期结果
        expect = get_expect(step_list[-1])

        case = [
            title,
            group,
            _author,
            "",
            steps,
            expect,
            u"功能测试",
            level
        ]

        case_list.append(case)

    return case_list


def get_expect(data):
    """
    处理预期结果，截掉优先级P0_
    :param data:
    :return:
    """

    if data[0].upper() == "P":
        return '【1】' + data[3:]
    else:
        return '【1】' + data


def get_level(last_str):
    """
    截取用例级别
    如果没写，返回空
    :param last_str:
    :return:
    """
    if last_str[0].upper() != "P":
        return ""
    else:
        return last_str[0:2]


def get_step_index(step_list):
    """
    获取Step标注的节点，在整个链路的索引
    如果没写Step，则返回0
    :param step_list:
    :return:
    """
    step_index = 0

    for step in step_list:
        if step[0:4].upper() == "STEP":
            step_index = step_list.index(step)

            break
    return step_index


def get_title(title):
    """
    截取用例标题，并以"-"连接
    :param title:
    :return:
    """
    length = len(title)
    result = ""
    for each in title:
        result = result + each

        index = title.index(each)

        if index < length - 1:
            result += "-"

    return result


def get_group(group):
    """
    截取用例分组，以"|"分割连接
    :param group:
    :return:
    """
    length = len(group)
    result = "APP版本|"
    for each in group:
        result = result + each

        index = group.index(each)

        if index < length-1:
            result += "|"

    return result


def get_step(steps):
    """
    截取Step，并添加编号【1】
    :param steps:
    :return:
    """
    result = ""
    for each in steps:
        index = steps.index(each)

        if index == 0:
            each = each[5:]

        result = result + "【" + str(index+1) + "】" + each

    return result


def get_leaf_path(root_topic, path):
    """
    获取每一个根节点的路径，以下划线"_"分隔
    :param root_topic:
    :param path:
    :return:
    """
    sub_topics = root_topic.getSubTopics()
    path = path + "#" + root_topic.getTitle()

    if sub_topics is None:
        path_list.append(path)
    else:
        for sub_topic in sub_topics:
            get_leaf_path(sub_topic, path)


def write_excel(case_list, output_file):
    """
    写excel文件
    :param case_list:
    :param output_file:
    :return:
    """
    wb = load_workbook(output_file)
    ws = wb.active

    for case in case_list:
        ws.append(case)

    wb.save(output_file)


def copy_template():
    """
    复制模版，生成新文件供写入
    文件名为当前时间
    :return:
    """
    new_name = time.strftime("%Y%m%d%H%M%S") + ".xlsx"
    shutil.copy2(template_name, new_name)

    return new_name


if __name__ == '__main__':
    args = sys.argv
    file_name = args[1]
    suffix = splitext(file_name)[1]
    _author = args[2]

    if suffix != ".xmind":
        print(u"文件名不正确：" + file_name)
    else:
        xmind_data = read_xmind(file_name)
        case_file = copy_template()
        write_excel(xmind_data, case_file)