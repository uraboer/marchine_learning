#coding:utf-8
#准备数据：归一化数值
# newValue=(oldValue-min)/(max-min)
from numpy import *


def autoNorm(dataSet):
    minVals=dataSet.min(0)  #参数0表示从列中选取
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals

    normDataSet=zeros(shape(dataSet))  #shape[0]读取矩阵第一维度的长度，zeros()新的元素全部为0的数组
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minVals,(m,1))  #tile()复制成mx1维的矩阵
    normDataSet=normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals
