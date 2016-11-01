#coding:utf-8

#准备数据：从文本中解析数据
#将文本记录转换为NumPy的解析程序
from numpy import zeros

def file2matrix(filename):
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)  #得到文件行数
    returnMat=zeros((numberOfLines,3))  #创建返回的NumPy矩阵，另一维默认全设为3
    classLabelVector=[]
    index=0

    #解析文件到列表
    for line in arrayOLines:
        line=line.strip()   #strip()截取所有回车字符
        listFromLine=line.split("\t")   #将整行数据分割成一个元素列表
        returnMat[index,:]=listFromLine[0:3]   #选取前3个存入特征矩阵中
        classLabelVector.append(int(listFromLine[-1]))   #索引值-1表示最后一列，存储元素类型为整形
        index+=1
    return returnMat,classLabelVector

datingDataMat,datingLabels=file2matrix("datingTestSet2.txt")
print datingDataMat,datingLabels[0:20]