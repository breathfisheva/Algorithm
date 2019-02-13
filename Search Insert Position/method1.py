'''
题目：
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.


思路1：
#和一般的二分查找不同，最后要获得index，所以不能去更新nums的内容，可以考虑不改变nums内容，则考虑使用下标控制。
#1.考虑在列表里的情况
#[1,3,5,6], 5
#[1] , 1

#2.考虑没有在列表的情况
#考虑在中间的情况 [1,3,5,6], 2
#考虑最大的情况 [1,3,5,6], 7
#考虑最小的情况 [1,3,5,6], 0
#因为我们这里有mid-1操作，所以考虑mid=0的时候的情况 [1,3], 0

'''



class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        left = 0
        right = len(nums) - 1

        while(left < right): #如果只有两个元素则mid=0，后面的操作会导致right = -1
            mid = left + int((right-left)/2)
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] == target:
                return mid

        if left==right:
            if nums[left]>=target: #需要等号，考虑 [1],1 情况
                return left
            else:
                return left+1
        else:
            return left


print(Solution().searchInsert([1],1))

