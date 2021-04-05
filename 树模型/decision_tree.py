import os,sys,time,random
import numpy as np
import pandas as pd

def entropy(data):
    '''
    p_list:各类别样本占比
    '''
    return -sum([pk*np.log2(pk) for pk in p_list])

def gain(data,attribute,value):
    '''
    data:数据
    attribute:属性
    value:属性取值
    '''
    pass

def gain_ration(data,attribute,value):
    '''
    data:数据
    attribute:属性
    value:属性取值
    '''
    pass

def gini_index(data,attribute,value):
    '''
    data:数据
    attribute:属性
    value:属性取值
    '''
    pass


if __name__ == '__main__':
    data = pd.DataFrame({
        "a":[0,0,0,1,1,1,2,2,2,2],
        "b":[1,2,1,2,1,2,1,2,1,2],
        "c":[3,3,3,2,2,2,2,2,1,1],
        "d":[1,2,1,2,1,2,1,2,1,2],
        "e":[0,0,0,0,0,1,1,1,1,1],
        "target":[0,1,1,2,0,2,1,1,0,1],
        })
    print(p_list,entropy(data))
