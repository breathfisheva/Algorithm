'''
二分查找法
method1，我们是每次取1/2，然后找到一个值 它的平方小于x，然后对这个x每次加1，直到+1后的值符合 它的平方小于x，它加1的平方大于x。
method2，我们用二分查找法，用left和right来表示范围，mid等于left，right的平均值（向下取整），
如果平均值大于x，则right=mid
如果平均值小于x，则left=mid
直到符合  mid*mid <= x and (mid+1)*(mid+1)>x
这样会减少计算量，不是加1加1，而是二分。
'''

class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        left = 1  #考虑到x为1的情况，设置left=1
        right = x

        while True:
            mid = int((left+right)/2)

            if mid*mid <= x and (mid+1)*(mid+1)>x:
                return mid
            elif mid*mid > x:
                right = mid
            elif mid*mid <x:
                left = mid

print(Solution().mySqrt(1))
