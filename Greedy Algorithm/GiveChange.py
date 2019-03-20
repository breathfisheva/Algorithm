'''
钱币找零问题
这个问题在我们的日常生活中就更加普遍了。假设1元、2元、5元、10元、20元、50元、100元的纸币分别有c0, c1, c2, c3, c4, c5, c6张。现在要用这些钱来支付K元，至少要用多少张纸币？
用贪心算法的思想，很显然，每一步尽可能用面值大的纸币即可。在日常生活中我们自然而然也是这么做的。在程序中已经事先将Value按照从小到大的顺序排好。

分解问题：
当还需要找N'钱的时候，选择一个纸币用来找零,这个纸币要小于还需要找的钱的值，而且这个纸币还有>0张

选择最优策略：
策略1：选择面值最大的纸币

'''


class Money(object):
    def __init__(self, value, amount):
        self.value = value
        self.amount = amount

def strategy(Moneys):
    max_value = 0
    index = -1
    for i in range(len(Moneys)):
        if Moneys[i].value > max_value and Moneys[i].amount > 0:  #最优解是钱币最大，同时数量不为0
            max_value = Moneys[i].value
            index = i
    return index

def greedy(Moneys , Totalchange):
    totalchange = Totalchange
    index = -1
    while totalchange > 0:
        index = strategy(Moneys)
        if index!=-1: #如果有最优解
            if Moneys[index].value <= totalchange: #看下最优解是否小于现在还需要找的零钱总数， 有的话，还剩下更新还需要找零的总数，以及这个钱币的个数
                print(Moneys[index].value)
                totalchange -= Moneys[index].value
                Moneys[index].amount -= 1
            else:   #如果最优解大于还需要找的零钱总数，把最优解从零钱列表里删除
                del Moneys[index]

if __name__ == '__main__':
    moneys = [Money(1,1), Money(2,1), Money(5,1), Money(10,2), Money(20,1)]
    greedy(moneys, 16)


