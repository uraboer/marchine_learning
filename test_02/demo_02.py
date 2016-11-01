#coding:utf-8

#  kNN算法
# 1.计算已知类别数据集中的点与当前点之间的距离
# 2.按照距离递增次序排列
# 3.选取与当前点距离最小的k各点
# 4.确定前k个点所在类别的出现频率
# 5.返回前k各点出现频率最高的类别作为当前点的预测分类


from numpy import *   #科学计算包
import operator   #运算符模块

#创建数据集和标签
def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels=['A','A','B','B']
    return group,labels

# k-近邻算法分类器
def classify0(inX,dataSet,labels,k):  #inX分类的输入向量，dataSet输入的训练样本集，labels标签向量，k选择最近邻的数目
    dataSetSize=dataSet.shape[0]   #shape[0]计算行，shape[1]计算列

    #距离计算，欧式距离
    diffMat=tile(inX,(dataSetSize,1))-dataSet  #tile()重复数组
    sqDiffMat=diffMat**2  #**幂
    sqDistances=sqDiffMat.sum(axis=1)  #axis=0表示一个向量相加，axis=1表示对应坐标相加
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()  #argsort函数返回的是数组值从小到大的索引值

    #选择距离最小的k个点
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1  #确定前k各距离最小元素所在的主要分类

    #item()方法把字典中每对key和value组成一个元组，并把这些元组放在列表中返回
    #operator.itemgetter(1)按照第二个元素的次序对元组进行排序
    # false默认升序，true降序
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]   #返回频率最高的元素标签


group,labels=createDataSet()
print classify0([0,0],group,labels,3)  #打印B
