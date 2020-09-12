# _*_coding:utf-8_*_
# author: pineapple
# date:   2020/9/12 下午4:10
# file    main.py


from func.caculate_proximity import main
from func.read_data import read_item
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ppi_data_filepath", required=True,
                        help="filepath of ppi data")
    parser.add_argument("--ad_filepath", required=True,
                        help="filepath of ad data")
    parser.add_argument("--target_filenames", required=True,
                        help="filepath of medinces")
    parser.add_argument("--random_times", default=2, type=int)
    args = parser.parse_args()
    target_filepath_list = read_item(args.target_filenames)
    target_z = {}
    for target_filepath in target_filepath_list:
        z = main(args.ppi_data_filepath, args.ad_filepath,
                 target_filepath, args.random_times)
        target_z[target_filepath] = z
    print target_z

