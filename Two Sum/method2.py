# 方法二：
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False

        #创建一个字典，存当前值的索引，以及 差值（target-当前值的值）。
        #遍历nums，如果差值在nums里，那就返回这个差值的索引，以及和这个差值匹配的值 dict[nums[i]]
        #如果差值不在nums，则把差值继续存到字典里。

        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]],i]
            else:
                dict[target - nums[i]] = i

s = Solution()
nums = [2,7,11,15]
print(s.twoSum(nums,9))