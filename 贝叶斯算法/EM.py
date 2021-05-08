import os,sys,time,random,math
import matplotlib.pyplot as plt

'''
假设有AB两枚硬币，正面向上概率分别为ΘA和θB，假设进行了5组实验，但不知道每次
实验使用的是哪一枚硬币进行的，使用EM算法进行含有隐含数据的迭代优化求解；
'''

# 实验数据如下，数字表示第i次实验中正面向上的次数
total = 5
data = [3,2,1,3,2]

# 随机初始化AB硬币的正面向上概率
theta_a = .15
theta_b = .88

print(data)
print(theta_a,theta_b)

a_list = [theta_a]
b_list = [theta_b]

# 迭代求解
while True:
    # E步：在当前参数下估计实验使用A和B的概率
    e_list = [((theta_a**d)*((1-theta_a)**(total-d)),(theta_b**d)*((1-theta_b)**(total-d))) for d in data]
    print(e_list)
    e_list = [(d[0]/sum(d),d[1]/sum(d)) for d in e_list]
    print(e_list)
    e_expect = [((e[0]*d,e[0]*(total-d)),(e[1]*d,e[1]*(total-d))) for d,e in zip(data,e_list)]
    print(e_expect)
    theta_a_ = sum([exp[0][0] for exp in e_expect])/sum([exp[0][0]+exp[0][1] for exp in e_expect])
    theta_b_ = sum([exp[1][0] for exp in e_expect])/sum([exp[1][0]+exp[1][1] for exp in e_expect])
    if abs(theta_a_-theta_a)+abs(theta_b_-theta_b) < 0.01:
        break
    theta_a,theta_b = theta_a_,theta_b_
    print(theta_a,theta_b)
    a_list.append(theta_a)
    b_list.append(theta_b)


plt.title("θA="+str(theta_a)+", θB="+str(theta_b))
plt.plot(a_list)
plt.plot(b_list)
plt.show()
