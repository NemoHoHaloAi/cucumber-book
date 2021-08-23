import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

'''
向量场：
    对于函数f(x)，如果该函数是未知的，但是能够确认n个点对应的f(x)上的切线，
    也就是知道f(x)的导数，那么能否反推出f(x)？？？

    很显然答案是可以的，这其实就是不定积分求解过程在做的事。
'''

# # meshgrid生成网格点矩阵坐标，即对整个二维平面划分为一堆的小格子，每个小格子对应的坐标
# # 对应到此处，其实就是最后画出来的每个箭头的x和y坐标
# # X为0到6.2的行堆叠的2d数组
# # Y为0到6.2的列堆叠的2d数组
# # U为2d数组X对应的cos(x)的2d数组
# # V为2d数组X对应的cos(y)的2d数组
# G,V0,Y0=9.8,3,1
# X, Y = np.meshgrid(np.arange(-1 * np.pi, 1 * np.pi, .2), np.arange(-1 * np.pi, 1 * np.pi, .2))
# # U = np.cos(X)
# # V = -np.sin(Y)
# # V2 = -np.cos(Y)
# U = -(1/2)*G*t^2+V0*t+Y0
# V = -G*t+V0
# V2 = -G
# step,L = 2,[]
# for x,u,v in zip(X[0,::step],U[0,::step],V[::step,0]):
#     print(x,u,x+step*.1,u+(v*step*.1))
#     L.append((x,0,x+step*.1,v*step*.1))
# 
# fig1, ax1 = plt.subplots()
# ax1.set_title('函数线素场')
# # ax1.plot(X[0],U[0],label="原函数")
# # ax1.plot(X[0],V[:,0],label="导函数")
# # for D in np.arange(-12,12,.2):
# #     for x,y,x1,y1 in L:
# #         ax1.plot([x,x1],[D+y,D+y1])
# Q = ax1.quiver(U, V, V, V2, units='inches')
# # plt.ylim(-4,4)
# plt.legend()
# 
# plt.show()
X, Y = np.meshgrid(np.arange(-5, 5, .2), np.arange(-5, 5, .2))
U = np.sin(X) + np.sin(Y)
V = np.sin(X) - np.sin(Y)
fig, ax = plt.subplots()
Q = ax.quiver(X,Y,U,V, units='xy')
plt.show()
