import numpy as np
import matplotlib.pyplot as plt

# 初始化图像绘制点及其对应时间，注意时间0到1为一个绘制周期，也就是e^2Πit的一个圆周运动
ft = [(2,1),(2,1),(1,1),(0,2),(-1,1),(-2,1),(-1,-1),(-1.5,-2),(0,-1),(1.5,-2),(1,-1),(2,1),(2,1)] # 0~1
ft = [(-1,-1),(0,1),(1,-1),(-1,-1)]
ft = [(5,3),(4,4),(3,3),(2,4),(1,3),(2,2),(3,1),(4,2),(5,3)]
t = [0+i*(1/(len(ft)-1)) for i in range(len(ft))]

# 绘制原始图形
plt.subplot(121)
plt.plot([f[0] for f in ft],[f[1] for f in ft])

# 给定参数n，计算复常数Cn
def fourier_series(n):
    res = 0
    for t_,ft_ in zip(t,ft):
        constants = complex(0,-n*2*np.pi*t_)
        ft_complex = complex(ft_[0],ft_[1])
        res += ft_complex*np.exp(constants)
    return res

# 给定N的范围，N越多表示使用越多正弦函数拟合图像
N = range(-100,100+1,1)
# N = range(-10,10+1,1)
# N = range(-5,5+1,1)
# N = range(-3,3+1,1)
# N = range(-2,2+1,1)
# N = range(-1,1+1,1)
C = []
for n in N:
    C.append(fourier_series(n))

x,y = [],[]
# for t_,ft_ in zip(t[1:-1],ft[1:-1]):
for t_,ft_ in zip(t,ft):
    print(t_,ft_)
    res = 0
    for n,c in zip(N,C):
        constants = complex(0,n*2*np.pi*t_)
        res += c*np.exp(constants)
    print("\t",res.real,res.imag)
    x.append(res.real/len(N))
    y.append(res.imag/len(N))
# FIXME
x[0],x[-1] = x[0]/2,x[-1]/2
y[0],y[-1] = y[0]/2,y[-1]/2
plt.subplot(122)
plt.plot(x,y)
plt.show()
