'''
题目：
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

思路：
取x/2看下 x/2 * x/2是否比x大，如果大的话，继续取一半一半的取,直到取到的值的平方小于x
        while True:
            if mid*mid > x:
                mid = int(mid/2)

然后判断x是否在mid*mid 和 (mid+1)*(mid+1）之间(包括mid+1的平方),如果是的话返回mid，不是的话，mid就不断加1
            elif mid*mid < x:
                if (mid+1) * (mid+1) <=x:
                    mid = mid+1
                else:
                    return mid

如果mid*mid就是x的值，那就直接返回mid

注意：
1.确认下我们的if判断是否涵盖了所有条件， >x, <x, ==x，
2.因为我们的mid是向下取整，所以要特别注意x=1的情况
mid = int((0+x)/2)

'''

class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        if x ==1:      #注意1要单独判断，判断mid = int(x/2)=0,会返回0
            return 1
        mid = int((x)/2)
        while True:
            if mid*mid > x:
                mid = int(mid/2)
            elif mid*mid < x:
                if (mid+1) * (mid+1) <=x: #注意要等于x  否则9的话就会返回2
                    mid = mid+1
                else:
                    return mid
            elif mid*mid == x:
                return mid
print(Solution().mySqrt(1))