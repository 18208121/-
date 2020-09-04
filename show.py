import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

sunspots = pd.read_csv(r'小米.csv')
print(len(sunspots['价格']))
list = []
for i in range(len(sunspots['价格'])):
    list.append(i+1)
y1 = sunspots['价格']
x1 = list
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('价格')
# 设置横坐标名称
ax1.set_xlabel('第几个商品')
# 设置纵坐标名称
ax1.set_ylabel('商品价格')
# 画散点图
ax1.scatter(x1, y1, s=20, c='k', marker='.')
plt.show()
