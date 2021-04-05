import os,sys,time,random
import numpy as np
import matplotlib.pyplot as plt

'''
y = w * x + b

假设属性只有一列，则可以通过对E(w,b)即数据点到直线的欧氏距离和针对w和b求导，并另两式为0得到w和b的计算公式，以得到最优解；
'''

_,axs = plt.subplots(2,3)
for idx,i in zip(range(6),[50,100,200,500,1000,2000]):
    ax = axs[idx//3][idx%3]
    range_ = range(i)
    rand = np.random.randint(-100,100,size=len(range_))
    # 注意：int数据在超过范围后会变为负数，尽量使用浮点型避免数据越界
    D = [(x*1.,(x+r)*1.) for x,r in zip(range_,rand)]
    
    X = [xy[0] for xy in D]
    Y = [xy[1] for xy in D]
    
    m = len(D)
    x_mean = np.mean(X)
    
    w = (np.sum([xy[1]*(xy[0]-x_mean) for xy in D ]))/(np.sum([x**2 for x in X])-(1/m)*((np.sum(X))**2))
    b = (1/m)*(np.sum([xy[1] - w*xy[0] for xy in D]))
    print(i,D[-1],m,x_mean,w,b)
    
    ax.set_title("y = "+str(w)[:5]+" * x + "+str(b)[:5])
    ax.scatter(X,Y,s=10)
    ax.plot(range_,[w*x+b for x in range_],c="r")
    
plt.show()
