#coding:utf-8

# k-近邻算法
# 优点：精度高、对异常值不敏感、无数据输入假定
# 缺点：计算复杂度高、空间复杂度高
# 适用数据范围：数值型和标称型

from numpy import *   #科学计算包
import operator   #运算符模块

#创建数据集和标签
def createDataSet():
    group=array([1.0,1.1],[1.0,1.0],[0,0],[0,0.1])
    labels=['A','A','B','B']
    return group,labels
