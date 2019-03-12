'''
抓了a,b,c,d四名犯罪嫌疑人，其中有一人是小偷，审讯中：

a说我不是小偷；
b说c是小偷；
c说小偷肯定是d；
d说c胡说！

其中有三个人说的是实话，一个人说的是假话，请编程推断谁是小偷（用穷举法和逻辑表达式）。
'''

sum = 0
for thief in ('a', 'b', 'c', 'd'):
    sum = ('a'!=thief) + ('c'==thief) + ('d'==thief) + (thief!='d')
    if sum==3 :
        print('thief is %s' %(thief))
