import os,sys
import numpy as np
import matplotlib.pyplot as plt

count = int(sys.argv[1])
num = int(sys.argv[2])

def c(c_,n_):
    result = 1
    for i in range(c_,c_-n_,-1):
        result *= i
    for i in range(n_,0,-1):
        result /= i
    return result

result_idx = [i for i in range(100,1000000,10)]
result = [c(count,num)*((count/i)**num)*((1-count/i)**(count-num)) for i in range(100,1000000,10)]

max_idx = np.argmax(result)
left = max_idx-100 if max_idx-100>=0 else 0
right = max_idx +100 if max_idx+100<=len(result) else len(result)

plt.plot(result_idx[left:right],result[left:right])

plt.show()
