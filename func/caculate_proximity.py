# _*_coding:utf-8_*_
# author: pineapple
# date:   2020/9/12 下午4:09
# file    caculate_proximity.py


import math
from collections import Counter
from random import sample
from random import seed
import numpy
import networkx as nx
from read_data import read_ppi_file
from read_data import read_item

def shortest_dist(graph, from_node, to_node):
    try:
        ans = nx.dijkstra_path_length(graph, from_node, to_node)
    except:
        ans = float("inf")
    finally:
        return ans

def caculate_w(s, t, degree, ad_data):
    if t in ad_data:
        d = degree[s]
        return -1 * math.log(d + 1)
    else:
        return 0


def caculate_proximity(s_list, t_list, degree_dict, G):
    ans = 0
    inf_num = 0
    for t in t_list:
        s_min = float("inf")
        for s in s_list:
            w = caculate_w(s, t, degree_dict, s_list)
            dist_s_w = shortest_dist(G, s, t)
            s_min = min(s_min, dist_s_w + w)
        if s_min == float("inf"):
            inf_num += 1
        else:
            ans += s_min
    return ans / (len(t_list) - inf_num)

def random_sample(all_nodes, n):
    return sample(all_nodes, n)


def main(ppi_data_file, ad_data_file, target_data_file, random_times):
    # read ppi file.
    g_data = read_ppi_file(ppi_data_file)

    # read ad-genes data and target genes data.
    ad_data = read_item(ad_data_file)
    target_data = read_item(target_data_file)

    # caculate the degree of ad-genes
    col1_dict = Counter([i[0] for i in g_data])
    col2_dict = Counter([i[1] for i in g_data])
    degree_dict = {}
    for k, v in col1_dict.items():
        degree_dict[k] = degree_dict.get(k, 0) + col1_dict[k]
    for k, v in col2_dict.items():
        degree_dict[k] = degree_dict.get(k, 0) + col2_dict[k]

    # Creating a network and caculating the shortest distance from node1 to node2.
    G = nx.Graph()
    G.add_edges_from(g_data)
    dist_S_T = caculate_proximity(ad_data, target_data, degree_dict, G)

    # sample R from network nodes.
    seed(1234)
    dist_list = []
    for i in range(random_times):
        r_list = random_sample(G.nodes(), len(target_data))
        dist_s_r = caculate_proximity(ad_data, r_list, degree_dict, G)
        dist_list.append(dist_s_r)

    dist_list_mean = numpy.mean(dist_list)
    dist_list_std = numpy.std(dist_list)
    Z = (dist_S_T - dist_list_mean) / dist_list_std
    return Z
