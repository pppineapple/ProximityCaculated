# _*_coding:utf-8_*_
# author: pineapple
# date:   2020/9/12 下午4:10
# file    main.py


from func.caculate_proximity import main
from func.read_data import read_item
from func.read_data import medicine_existd_ppi
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
    parser.add_argument("--output", required=True,
                        help="filepath of output")
    args = parser.parse_args()
    target_filepath_list = read_item(args.target_filenames)
    target_z = {}
    with open(args.output, "w") as f:
        for target_filepath in target_filepath_list:
            if medicine_existd_ppi(target_filepath, args.ppi_data_filepath):
                z = main(args.ppi_data_filepath, args.ad_filepath,
                         target_filepath, args.random_times)
                target_z[target_filepath] = z
            else:
                target_z[target_filepath] = None
            f.writelines("{0},{1}\n".format(target_filepath, target_z[target_filepath]))
    print target_z

    # order_target_z_key = sorted(target_z.keys())
    # with open(args.output, "w") as f:
    #     for k in order_target_z_key:
    #         f.writelines("{0},{1}\n".format(k, target_z[k]))


