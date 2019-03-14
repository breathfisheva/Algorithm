'''
只有一艘船，能乘2人，船的运行速度为2人中较慢一人的速度，过去后还需一个人把船划回来，问把n个人运到对岸，最少需要多久。

策略1：最快的和次快的过河，然后最快的将船划回来；次慢的和最慢的过河，然后次快的将船划回来，所需时间为：t[0]+2*t[1]+t[n-1]；
策略2：最快的和最慢的过河，然后最快的将船划回来，最快的和次慢的过河，然后最快的将船划回来，所需时间为：2*t[0]+t[n-2]+t[n-1]。
'''
#策略1
def greedy1(timelist):
    total_time = 0
    length = len(timelist)

    #当有多个人的时候
    while(length>3):
        total_time += timelist[0]+2*timelist[1]+timelist[length-1]
        length -= 2 #每次送过去两人

    #当只有三个人的时候，按照策略1一定是剩下前三快的
    if (length == 3):
        total_time += timelist[0] + timelist[1] + timelist[2]

    # 当只有两个人的时候，按照策略1一定是剩下前二快的
    elif(length == 2):
        total_time += timelist[1]

    #当只有一个人的时候，按照策略1一定是剩下最快的
    else:
        total_time += timelist[0]

    print(total_time)

#策略2
def greedy2(timelist):
    total_time = 0
    length = len(timelist)

    #当有多个人的时候
    while(length>3):
        total_time += timelist[length-2]+2*timelist[0]+timelist[length-1]
        length -= 2 #每次送过去两人

    #当只有三个人的时候，按照策略2一定是剩下前三快的
    if (length == 3):
        total_time += timelist[0] + timelist[1] + timelist[2]

    # 当只有两个人的时候，按照策略2一定是剩下前二快的
    elif(length == 2):
        total_time += timelist[1]

    #当只有一个人的时候，按照策略2一定是剩下最快的
    else:
        total_time += timelist[0]

    print(total_time)

if __name__ == '__main__':
    timelist = [1,4,5,8]
    greedy1(timelist)
    greedy2(timelist)

