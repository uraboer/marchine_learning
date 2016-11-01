#coding:utf-8
#分析数据：使用Matplotlib创建散点图

import matplotlib
import matplotlib.pyplot as plt
from numpy import array

from test_02.demo_03 import datingDataMat, datingLabels

fig=plt.figure()
ax=fig.add_subplot(111)   #add_subset(111)表示1x1的网格，优先子区
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))

plt.show()