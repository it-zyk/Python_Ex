# coding=utf-8

import matplotlib.pyplot as plt


# ----------------------使用Scatter()绘制一系列点----
# x_value = [1, 2, 3, 4, 5]
# y_value = [1, 4, 9, 16, 25]
x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, c=y_value,
            cmap=plt.cm.Blues, edgecolor='none', s=40)
# plt.scatter(x_value, y_value, c='red', edgecolor='none', s=40)
# plt.scatter(x_value, y_value,c=(0,0,0.8),edgecolor='none', s=40)

plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('square_png',bbox_inches='tight')
plt.show()
