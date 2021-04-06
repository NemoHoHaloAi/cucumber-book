import numpy as np
import matplotlib.pyplot as plt

'''
感知机口袋算法：与暴力法不同，口袋算法提供了两项改动，首先通过epochs控制完整的数据训练次数，其次同步保存目前的最优w和b，这使得它可以在有限次数内处理可分和不可分情况；
'''

# 初始化 w 和 b，np.array 相当于定义向量
w,b = np.array([0, 0]),0 

# 定义点积函数
def d(x):
    return np.dot(w,x)+b # np.dot 是向量的点积

# 定义符号函数
def sign(y):
    return 1 if y>=0 else -1

# 定义误差评分函数
def score(X,y,w,b):
    return sum([yi*sign(d(xi)) for xi,yi in zip(X,y)])

# 历史信用卡发行数据，该数据不是线性可分的
X = np.array([[5,2], [3,2], [2,7], [1,4], [6,1], [4,5], [2,4.5]])
y = np.array([-1, -1, 1, 1, -1, 1, -1, ])

best_w,best_b,best_score = w,b,score(X,y,w,b)
epochs = 10
for _ in range(epochs):
    for xi,yi in zip(X,y):
        if yi*d(xi)<=0:
            w,b = w+yi*xi,yi+b
            if score(X,y,w,b) > best_score:
                best_w,best_b = w,b
            break

print(best_w,best_b)

positive = [xi for xi,yi in zip(X,y) if yi==1]
negative = [xi for xi,yi in zip(X,y) if yi==-1]
line = [(-w[0]*x-b)/w[1] for x in [-100,100]]
plt.title('w='+str(w)+', b='+str(b))
plt.scatter([x[0] for x in positive],[x[1] for x in positive],c='green',marker='o')
plt.scatter([x[0] for x in negative],[x[1] for x in negative],c='red',marker='x')
plt.plot([-100,100],line,c='black')
plt.xlim(min([x[0] for x in X])-1,max([x[0] for x in X])+1)
plt.ylim(min([x[1] for x in X])-1,max([x[1] for x in X])+1)

plt.show()
