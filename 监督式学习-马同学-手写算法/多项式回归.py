import numpy as np
from 线性回归最小二乘法矩阵实现 import LinearRegression as LR

class PolynomialRegression(LR):
    def __init__(self,X,y,degress=1):
        self.degress = degress
        X = np.hstack([X**deg for deg in range(1,degress+1)])
        super(PolynomialRegression,self).__init__(X,y)

    def predict(self,x):
        x = np.array([x**deg for deg in range(1,self.degress+1)])
        return super(PolynomialRegression,self).predict(x)
