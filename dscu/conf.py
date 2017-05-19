"""
file: conf
author: fupeng
date: 2017/5/5


"""
import sys
sys.path.append('../')
import os
import logging
import sklearn
if sklearn.__version__ == '0.18.1':
    from sklearn.model_selection import KFold
else:
    from sklearn.cross_validation import KFold


path = "../data/"
if not os.path.isdir(path):
    os.makedirs(path)

logging_path = "./"
if not os.path.isdir(logging_path):
    os.makedirs(logging_path)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=logging_path + 'logging.log',
                    filemode='a+')
