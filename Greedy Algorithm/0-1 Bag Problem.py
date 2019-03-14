'''
有一个背包，最多承载重量为C=150的物品，现在有7个物品（物品不能分割成任意大小），编号为1~7，重量为 wi = [35,30,60,50,40,10,25] ,
价值分别为pi = [10,40,30,50,35,40,30]，现在从这7个物品中选择一个或多个装入背包，要求在物品总量不超过C的前提下，所装入的物品总价值最高。

策略1：根据物品的价值选择，每次选择价值最高的
策略2：根据物品的重量选择，每次选择最轻的
策略3：根据物品的价值密度（价值/重量）选择，每次选择价值密度最大的。
'''

#1.物品数据结构
class Good(object):
    def __init__(self, weight, value, status):
        self.weight = weight
        self.value = value
        self.status = status  #0:未选中； 1：已选中； 2：已经不可选

#2.背包数据结构
class Bag(object):
    def __init__(self, goods, totalC):
        self.goods = goods #物品列表
        self.totalC = totalC #背包的承重

#3.局部最优选择策略
def stategy(goods, total): #策略1：根据物品的价值选择，每次选择价值最高的
    index = -1
    maxvalue = 0
    for i in range(len(goods)):
        if (goods[i].status == 0 and goods[i].value > maxvalue):
            maxvalue = goods[i].value
            index = i
    return index

#4.贪心算法
def greedyAlgo(bag, stategy):
    ntotalc = 0 #用来存放已经放入背包的物品总的重量

    while True:
        index = stategy(bag.goods, bag.totalC-ntotalc) #局部最优值的index
        if (index!=-1): #如果能找到局部最优的值则继续
            if(ntotalc + bag.goods[index].weight < bag.totalC): #判断新加的物品加上已经在背包的物品的总重量是否小于背包的承载
                bag.goods[index].status = 1 #收入背包，状态设为1
                ntotalc += bag.goods[index].weight #背包物品重量增加
            else:
                bag.goods[index].status = 2 #新加上这个物品后总重量超过背包承载则状态设为2
        else:
            break
    for i in range(len(bag.goods)):
        print(bag.goods[i].status)


if __name__ == '__main__':
    goods = [Good(35,10,0), Good(30,40,0), Good(60,30,0), Good(50,50,0), Good(40,35,0), Good(10,40,0), Good(25,30,0)]
    totalC = 150
    bag = Bag(goods, totalC)
    greedyAlgo(bag, stategy)







