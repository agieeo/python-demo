# 4.1 数据的爬取
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
file_path=open(r'graph.csv')
local_data=pd.read_csv(file_path)


# 4.2河北省景点面积和旅客量位居前三的条形图显示
area=float("{:.1f}".format(local_data['总面积(平方公里)'].mean()))
# 计算游客数量的平均值
tour=float("{:.1f}".format(local_data['游客量(万人次)'].mean()))
#使用字典映射的方式进行填充数据
dic={'总面积(平方公里)':area,"游客量(万人次)":tour}
addata=local_data.fillna(value=dic)
addata.head()
dic={'总面积(平方公里)':area,"游客量(万人次)":tour}
addata=local_data.fillna(value=dic)
data=addata.groupby("省份")
# 显示河北地区的·数据
hebei=dict([x for x in data])['河北']

# 需要我们绘制直方图

#为正常显示中文字体，添加的代码
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# 显示的数据选取
area=hebei["总面积(平方公里)"].values
tour=hebei["游客量(万人次)"].values
# 设置图像的大小
plt.figure(figsize=(12,6))
x_num=range(0,len(area))
x_dis=[i + 0.3 for i in x_num]
plt.bar(x_num,area,color='g',width=.3,label='总面积')
plt.bar(x_dis,tour,color='r',width=.3,label='游客量')

#增加x、y轴文字说明
plt.ylabel("单位：平方千米、万人次")
plt.title("河北旅游景点面积以及游客数量")
# 设置图例
plt.legend(loc="upper right")
plt.xticks(range(0,10),['苍岩山','嶂石岩','西柏坡-天桂山','秦皇岛北戴河','响堂山','娲皇宫','太行大峡谷','崆山白云洞','野三坡','承德避暑山庄外八庙'])
plt.show()




