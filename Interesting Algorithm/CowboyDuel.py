'''
三个牛仔参加决斗，他们在同一时间开枪射击，假设每一个牛仔随机选择射击另两个牛仔，并且百分之百可以击中。
请问这三个牛仔，至少有一个能够毫发未损的几率。
'''

round = 0
suvived = 0

for i in ['a', 'b']:
    for j in ['b', 'c']:
        for k in ['a', 'c']:
            round += 1
            if 'a'!=i and 'a'!=j and 'a'!=k :
                suvived += 1
            elif 'b'!= i and 'b'!= j and 'b'!= k:
                suvived += 1
            elif 'c' != i and 'c' != j and 'c' != k:
                suvived += 1
print(suvived/round)
