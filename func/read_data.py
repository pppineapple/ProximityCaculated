# _*_coding:utf-8_*_
# author: pineapple
# date:   2020/9/12 下午4:07
# file    read_data.py


def read_ppi_file(filepath):
    g_data = []
    with open(filepath, "r") as f:
        tmp_data = f.readline()
        while tmp_data:
            tmp = tuple(tmp_data.strip().split(","))
            g_data.append(tmp)
            tmp_data = f.readline()
    return g_data


def read_item(filepath):
    with open(filepath, "r") as f:
        data_list = map(lambda x: x.strip(), f.readlines())
    return data_list
