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


def medicine_existd_ppi(medi_filepath, ppi_filepath):
    target_data = read_item(medi_filepath)
    g_data = read_ppi_file(ppi_filepath)
    g_data_list = []
    for g1, g2 in g_data:
        if g1 not in g_data_list:
            g_data_list.append(g1)
        if g2 not in g_data_list:
            g_data_list.append(g2)

    if set(target_data) & set(g_data_list):
        return True
    else:
        return False
