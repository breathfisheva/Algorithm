'''
思路2：
因为nums是从小到大排列，我们从小到大和target比较，所以一旦target小于当前的nums[i],那它一定小于后面的数字，直接返回i
如果target大于当前的nums[i],则不断的看下一个元素,如果到最后一个元素target还是大于当前的nums[i]，此时还是 i = i + 1, 然后在循环之外return i的值
'''


class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        i = 0
        while(i < len(nums)):
            if nums[i]>=target:
                return i
            else:
                i = i + 1
        return i

print(Solution().searchInsert([1], 0))