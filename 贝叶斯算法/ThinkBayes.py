import os,sys,time,random
import matplotlib.pyplot as plt

class Pmf(object):
    '''
    概率质量函数
    '''

    def __init__(self):
        self.dict_ = {}

    def set(self,item,prob):
        '''
        初始化先验概率
        '''
        self.dict_[item] = prob

    def mult(self,item,likelihood):
        '''
        通过似然度更新概率值
        '''
        self.dict_[item] = self.dict_[item]*likelihood

    def normalize(self):
        '''
        归一化处理
        '''
        total = sum([self.dict_[k] for k in self.dict_.keys()])
        self.dict_ = {k:self.dict_[k]/total for k in self.dict_.keys()}

    def prob(self,item):
        return self.dict_[item]

    def values(self):
        return self.dict_.keys()

    def items(self):
        return self.dict_.items()

    def percentile(self,percentage):
        '''
        获取后验分布的百分位数，可用于置信区间
        '''
        percentage = percentage/100.0
        x = 0
        for val,prob in self.dict_.items():
            if x+prob>=percentage:
                return val
            x += prob

    def mean(self):
        '''
        后验分布的平均值
        '''
        return sum([k*v for k,v in self.dict_.items()])

class Suite(Pmf):

    def __init__(self,hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.set(hypo,1)
        self.normalize()

    def likelihood(self,data,hypo):
        pass

    def update(self,data):
        for hypo in self.values():
            like = self.likelihood(data,hypo)
            self.mult(hypo,like)
        self.normalize()

    def print(self):
        for hypo,prob in self.items():
            print('',hypo,prob)
        print()


class Cookie(Pmf):
    '''
    曲奇饼问题
    '''

    mixes = {
            'Bowl1':dict(vanilla=.75,chocolate=.25),
            'Bowl2':dict(vanilla=.5,chocolate=.5),
            }

    def __init__(self,hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.set(hypo,1)
        self.normalize()

    def likelihood(self,data,hypo):
        '''
        计算P(D|H)，对于曲奇饼问题，则是在已知是哪个碗的条件下获取某个口味饼干的概率；
        已知条件D为拿到了一个香草曲奇饼
        '''
        mix = self.mixes[hypo]
        like = mix[data]
        return like

    def update(self,data):
        for hypo in self.values():
            like = self.likelihood(data,hypo)
            self.mult(hypo,like)
        self.normalize()

class MontyHall(Pmf):
    '''
    蒙蒂大厅问题
    '''

    def __init__(self,hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.set(hypo,1)
        self.normalize()

    def likelihood(self,data,hypo):
        '''
        计算P(D|H)，对于蒙蒂大厅问题，则是若假设有奖品的门为B，则事件D发生的概率为0，因为如果B有奖品，那么是不能打开它的，若假设有奖品的门为A，则蒙蒂可以在B和C之间任意打开一个，则事件D发生的概率为1/2，若假设有奖品的门是C，则蒙蒂只能打开B，所以概率为1；
        已知条件D为蒙蒂打开了B门，且奖品不在门后
        '''
        if data==hypo:
            return 0
        elif hypo=='A':
            return .5
        else:
            return 1

    def update(self,data):
        for hypo in self.values():
            like = self.likelihood(data,hypo)
            self.mult(hypo,like)
        self.normalize()

class MontyHall2(Suite):
    def likelihood(self,data,hypo):
        if data==hypo:
            return 0
        elif hypo=='A':
            return .5
        else:
            return 1

class M_M(Suite):
    datas = {
            94:dict(褐色=.3,黄色=.2,红色=.2,绿色=.1,橙色=.1,黄褐色=.1),
            96:dict(褐色=.13,黄色=.14,红色=.13,绿色=.2,橙色=.16,蓝色=.24),
            }
    def likelihood(self,data,hypo):
        '''
        计算P(D|H)，对于M&M问题，则是若假设黄色是94，绿色是96，那么拿到黄色/绿色的概率，若假设黄色是96，绿色是94，那么拿到黄色/绿色的概率；
        已知条件D为从两个袋子中各取出一个巧克力豆，一个为黄色，一个为绿色；
        例如：
            首先是黄色
                P(黄色|假设A)即在94年的袋子中黄色巧克力的概率，已知为0.2
                P(黄色|假设B)即在96年的袋子中黄色巧克力的概率，已知为0.14
            其次是绿色
                P(绿色|假设A)即在94年的袋子中绿色巧克力的概率，已知为0.1
                P(绿色|假设B)即在96年的袋子中绿色巧克力的概率，已知为0.2
        这里可以看出这种处理方式是可以增量的增加条件的，这个特性很符合将贝叶斯用于机器学习领域，即通过不断更新的数据来更新条件概率；
        '''
        hypo = hypoes[hypo]
        return self.datas[hypo[data]][data]

class Dice(Suite):
    def likelihood(self,data,hypo):
        '''
        计算P(D|H)，对于骰子问题，任意面的骰子，只要得到的数字不超过骰子的面数，那么该骰子获得该数字的概率均可认为是1/骰子面数；
        已知条件D为扔出的骰子数；
        '''
        if data > hypo:
            return 0
        return 1/hypo

class Train(Suite):
    def likelihood(self,data,hypo):
        '''
        计算P(D|H)，火车头问题类似骰子问题；
        '''
        if data > hypo:
            return 0
        return 1/hypo

class Train2(Suite):
    def __init__(self,hypos,alpha=1.0):
        '''
        服从幂律分布的先验概率：PMF(x)∝(1/x)^a
        '''
        Pmf.__init__(self)
        for hypo in hypos:
            self.set(hypo,hypo**(-alpha))
        self.normalize()

    def likelihood(self,data,hypo):
        '''
        计算P(D|H)，火车头问题类似骰子问题；
        '''
        if data > hypo:
            return 0
        return 1/hypo

class Coin(Suite):
    def likelihood(self,data,hypo):
        '''
        计算P(D|H)，假设为硬币正面朝上的概率
        已知条件D表示140次正面110次反面
        '''
        return (hypo**(data))*((1-hypo)**(250-data))

if __name__ == '__main__':
    print('Cookie:')
    hypos = ['Bowl1','Bowl2']
    cookie = Cookie(hypos)
    cookie.update('vanilla')
    for hypo,prob in cookie.items():
        print('',hypo,prob)
    print()

    print('Monty Hall:')
    hypos = ['A','B','C']
    montyhall = MontyHall(hypos)
    montyhall.update('B') # 打开了B门
    for hypo,prob in montyhall.items():
        print('',hypo,prob)
    print()

    print('Monty Hall by Suite:')
    montyhall = MontyHall2('ABC') # 给出全部假设
    montyhall.update('B') # 更新条件D，这一步同时会计算P(D|H)，即不同假设下条件D的发生概率
    montyhall.print()

    print('M&M:')
    hypoes = dict(A=dict(黄色=94,绿色=96),B=dict(黄色=96,绿色=94))
    mm = M_M('AB')
    mm.update('黄色')
    mm.update('绿色')
    mm.print()

    print("Dice:")
    dice = Dice([4,6,8,12,20])
    dice.update(4)
    dice.print()
    for num in [6,8,7,7,5,4]:
        dice.update(num)
    dice.print()

    print("Train:")
    train = Train(range(1,1000)) # 假设有1、2、3、4、、、1000个火车头
    train.update(60)
    plt.title('P(H|D) mean:'+str(train.mean()))
    plt.plot([k for k,v in train.items()],[v for k,v in train.items()])
    train = Train(range(1,500)) # 假设有1、2、3、4、、、500个火车头
    train.update(60)
    plt.title('P(H|D) mean:'+str(train.mean()))
    plt.plot([k for k,v in train.items()],[v for k,v in train.items()])
    # plt.show()
    train = Train(range(1,1000)) # 假设有1、2、3、4、、、1000个火车头
    train.update(60)
    train.update(30)
    train.update(80)
    plt.title('P(H|D) mean:'+str(train.mean()))
    plt.plot([k for k,v in train.items()],[v for k,v in train.items()])
    train = Train(range(1,500)) # 假设有1、2、3、4、、、500个火车头
    train.update(60)
    train.update(30)
    train.update(80)
    plt.title('P(H|D) mean:'+str(train.mean()))
    plt.plot([k for k,v in train.items()],[v for k,v in train.items()])
    # plt.show()

    print("Train2:")
    train = Train2(range(1,1000)) # 假设有1、2、3、4、、、1000个火车头
    train.update(60)
    plt.title('P(H|D) mean:'+str(train.mean()))
    plt.plot([k for k,v in train.items()],[v for k,v in train.items()])
    train = Train(range(1,1000)) # 假设有1、2、3、4、、、1000个火车头
    train.update(60)
    print("","90%置信区间："+str((train.percentile(5),train.percentile(95))))
    plt.title('P(H|D) mean:'+str(train.mean()))
    plt.plot([k for k,v in train.items()],[v for k,v in train.items()])
    plt.show()

    print("Coin:")
    coin = Coin([i/100. for i in range(1,101,1)])
    coin.update(140)
    print("","90%置信区间："+str((coin.percentile(5),coin.percentile(95))))
    plt.title('P(H|D) mean:'+str(coin.mean()))
    plt.plot([k for k,v in coin.items()],[v for k,v in coin.items()])
    plt.show()
