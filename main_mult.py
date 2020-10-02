# _*_coding:utf-8_*_
# author: pineapple
# date:   2020/9/12 下午4:10
# file    main.py


from func.caculate_proximity import main
from func.read_data import read_item
from func.read_data import medicine_existd_ppi
import argparse


if __name__ == "__main__":


    random_times = 2
    target_filenames = "PPI/target_filenames"
    target_filepath_list = read_item(target_filenames)
    ad_list = [
        ("PPI/disease_cluster1.txt", "PPI/PPI_cluster1.txt", "output_cluster1_test.csv"),
        ("PPI/disease_cluster2.txt", "PPI/PPI_cluster2.txt", "output_cluster2_test.csv"),
        ("PPI/disease_cluster3.txt", "PPI/PPI_cluster3.txt", "output_cluster3_test.csv"),
        ("PPI/disease_cluster4.txt", "PPI/PPI_cluster4.txt", "output_cluster4_test.csv"),
        ("PPI/disease_cluster5.txt", "PPI/PPI_cluster5.txt", "output_cluster5_test.csv"),
    ]

    for ad_filepath, ppi_data_filepath, output in ad_list:
        target_z = {}
        with open(output, "w") as f:
            for target_filepath in target_filepath_list:
                if medicine_existd_ppi(target_filepath, ppi_data_filepath):
                    z = main(ppi_data_filepath, ad_filepath,
                             target_filepath, random_times)
                    target_z[target_filepath] = z
                else:
                    target_z[target_filepath] = None
                f.writelines("{0},{1}\n".format(target_filepath, target_z[target_filepath]))
        print target_z




