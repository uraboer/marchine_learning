#coding:utf-8
#分析数据：使用Matplotlib创建散点图

import matplotlib
import matplotlib.pyplot as plt
from numpy import *

from test_02.demo_03 import datingDataMat, datingLabels

fig=plt.figure()
ax=fig.add_subplot(121)   #add_subset(111)表示1x1的网格，优先子区
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels)) #色彩，尺寸

zhfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc') #宋体
plt.xlabel(u"玩视频游戏所耗时间百分比",fontproperties=zhfont)
plt.ylabel(u"每周消费的冰淇淋公升数",fontproperties=zhfont)

#采用列1，2的属性值效果更好
ax=fig.add_subplot(122)
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
zhfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
plt.xlabel(u"每年获取的飞行常客里程数",fontproperties=zhfont)
plt.ylabel(u"玩视频游戏所耗时间百分比",fontproperties=zhfont)

plt.show()



###加入图例，自定义坐标轴
fig=plt.figure()
axes = plt.subplot(111)
# 将三类数据分别取出来
# x轴代表飞行的里程数
# y轴代表玩视频游戏的百分比
type1_x = []
type1_y = []
type2_x = []
type2_y = []
type3_x = []
type3_y = []

for i in range(len(datingLabels)):   #1,2,3
    if datingLabels[i] == 1:  # 不喜欢
        type1_x.append(datingDataMat[i][0])
        type1_y.append(datingDataMat[i][1])

    if datingLabels[i] == 2:  # 魅力一般
        type2_x.append(datingDataMat[i][0])
        type2_y.append(datingDataMat[i][1])

    if datingLabels[i] == 3:  # 极具魅力
        type3_x.append(datingDataMat[i][0])
        type3_y.append(datingDataMat[i][1])

type1 = axes.scatter(type1_x, type1_y, s=20, c='red')
type2 = axes.scatter(type2_x, type2_y, s=40, c='green')
type3 = axes.scatter(type3_x, type3_y, s=50, c='blue')

plt.xlabel(u'每年获取的飞行里程数', fontproperties=zhfont)
plt.ylabel(u'玩视频游戏所消耗的事件百分比', fontproperties=zhfont)
axes.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2, prop=zhfont)
plt.show()