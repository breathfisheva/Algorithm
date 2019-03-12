'''
农夫需要把狼、羊、菜和自己运到河对岸去，只有农夫能够划船，而且船比较小，除农夫之外每次只能运一种东西，还有一个棘手问题，就是如果没有农夫看着，羊会偷吃菜，狼会吃羊。
请考虑一种方法，让农夫能够安全地安排这些东西和他自己过河。
'''

animal = ['wolf', 'sheep', 'green']
for first in ('wolf', 'sheep', 'green'):
    for second in ('wolf', 'sheep', 'green'):
        for third in ('wolf', 'sheep', 'green'):
            if (second == 'sheep' and third == 'green') or (second == 'green' and third == 'sheep'): #羊会偷吃菜
                pass
            elif (second == 'wolf' and third == 'sheep') or (second == 'sheep' and third == 'wolf'): #狼会吃羊
                pass
            elif (first!=second and second!=third and first!=third): #每次带的动物不能重复
                print(first, second, third)
