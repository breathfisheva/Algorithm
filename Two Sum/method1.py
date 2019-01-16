#问题：
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


#方法一：
class Solution:
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # self.nums = nums
        # self.target = target

        length = len(nums)
        if length < 2:
            return False
        else:
            for i in range(length):
                for j in range(i+1,length):
                    if nums[i] + nums[j] == target:
                        return [i,j]
s = Solution()
nums = [2,7,11,15]
print(s.twoSum(nums,9))