# Proximity Caculated


A repo for caculating Network-based proximity between drugs and AD-genes.

This repository contains:

1. [Caculating the Proximity](func/caculate_proximity.py)
2. How to use it.


## Table of Contents

- [Background](#Background)
- [Install](#install)
    - [Dependency](#dependency)
- [Usage](#usage)
    - [Repo Dir Description](#repo-dir-description)
    - [Example](#example)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

My friend, a medical student, has been suffered from the trouble about how to caculate proximity about drugs and AD-genes in her project. when I heard her problem, maybe it's not difficult to use python to figure it out. So we decided to beat it, and we solved this problem after readed papers, discussed the formula，debated for it's idea, and fixed some coding bug. This is very cool experenice!

## Install

It is out of the box. The latest release is [proximity_caculated-v1.0.0](https://github.com/pppineapple/ProximityCaculated/releases/tag/v1.0.0)

### Dependency
This repo is based on python2.7.

You need to install some python packages as below:

| Name     | Version   | Install Command           | Packages Pypi Site                     |
|:--------:|:---------:|:-------------------------:|:--------------------------------------:|
| networkx | 1.9       | pip install networkx==1.9 | https://pypi.org/project/networkx/1.9/ |
| numpy    | 1.8.0     | pip install numpy==1.8.0  | https://pypi.org/project/numpy/1.8.0/  |


## Usage

### Repo Dir Description

```
├─ images                      # some images in README.md
├─ func                        
│   ├─ caculate_proximity.py   # proximity caculated func
│   └─ read_data.py            # import data func
├─ data
│   ├─ disease_cluster.txt     # disease genes
│   ├─ PPI_cluster.txt         # PPI genes
│   ├─ target_filenames        # medicine filename list
│   ├─ medicine1               # target genes for medicine1
│   └─ medicine2               # target genes for medicine2
├─ main.py                     # main script of caculating proximity for example data
└─ README.md
```

*   `func/caculate_proximity.py`: The formula is as below, and it comes from the paper ([Screening novel drug candidates for Alzheimer’s disease
by an integrated network and transcriptome analysis](https://academic.oup.com/bioinformatics/advance-article-abstract/doi/10.1093/bioinformatics/btaa563/5855131))
       
    >     
    >    <a href="https://www.codecogs.com/eqnedit.php?latex=d(S,&space;T)=\frac{1}{|T|}\sum_{t\epsilon&space;T}^{}min_{s\epsilon&space;S}(d(s,&space;t)&space;&plus;&space;w)" target="_blank"><img src="https://latex.codecogs.com/png.latex?d(S,&space;T)=\frac{1}{|T|}\sum_{t\epsilon&space;T}^{}min_{s\epsilon&space;S}(d(s,&space;t)&space;&plus;&space;w)" title="d(S, T)=\frac{1}{|T|}\sum_{t\epsilon T}^{}min_{s\epsilon S}(d(s, t) + w)" /></a>  
    >                                                                                                                                                                                                                                                                                                                             
    >    <a href="https://www.codecogs.com/eqnedit.php?latex=z(S,&space;T)&space;=&space;\frac{d(S,&space;T)-\mu&space;_{d(S,R)}}{\sigma&space;_{d(S,&space;R)}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?z(S,&space;T)&space;=&space;\frac{d(S,&space;T)-\mu&space;_{d(S,R)}}{\sigma&space;_{d(S,&space;R)}}" title="z(S, T) = \frac{d(S, T)-\mu _{d(S,R)}}{\sigma _{d(S, R)}}" /></a>

*   `data/target_filenames`: This file is made of a list of medicine. So how many medincine you put  in this file, how many medincine genes file you must put in data directory.
*   Attention: There are two choice about how to make a correct `data/target_filenames` and make sure it will be work:
    *   Using relative path about `medicine file` and `main.py`, such as `data/medicine1` in `data/target_filenames` I made.
    *   Using absolute path about `medicine file`, such as `/Users/pineapple/PycharmProjects/xpp/data/medicine1`


## Example

```sh
python main.py --help
usage: main.py [-h] --ppi_data_filepath PPI_DATA_FILEPATH --ad_filepath
               AD_FILEPATH --target_filenames TARGET_FILENAMES
               [--random_times RANDOM_TIMES]

optional arguments:
  -h, --help            show this help message and exit
  --ppi_data_filepath   filepath of ppi data
  --ad_filepath         filepath of ad data
  --target_filenames    filepath of medinces
  --random_times        random sample size, default is 2
```

```sh
python2.7 main.py --ppi_data_filepath data/PPI_cluster.txt --ad_filepath data/disease_cluster.txt --target_filenames data/target_filenames
>>> {'data/medicine2': 1.9894987751650182, 'data/medicine1': 2.2067697024924824}
```

The output about `{'data/medicine2': 1.9894987751650182, 'data/medicine1': 2.2067697024924824}` means:
*   Z value of medicine2 is 1.9894987751650182
*   Z value of medicine1 is 2.2067697024924824

## Maintainers

[@pppineapple](https://github.com/pppineapple)

### Contributors

This project exists thanks to my friend,a trouber maker, who contribute but dosen't has github account. 

![xpp](images/xpp_small.png)

## License

[MIT](LICENSE) © pppineapple
