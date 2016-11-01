#coding:utf-8
from numpy import  *

print type(random.rand(4,4))  #随机数组

print type(mat(random.rand(4,4)))   #mat()转化为矩阵

print mat(random.rand(4,4)).I  #.I求逆矩阵

randMat=mat(random.rand(4,4))
invRandMat=randMat.I
print randMat*invRandMat   #对角线为1，其余为0，有误差

print eye(4)   #单位矩阵
