'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

思路：
两重循环，如果相加等于target则返回index

注意：
1.[0,0,3,4] , 0  ，注意这种情况如果排除重复的可能会输出[1,1]，而我们期望的是[1,2]
'''

# numbers = [2,7,11,15], target = 9  [1,2]

class Solution:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':

        for i in range(len(numbers)):
            difference = target - numbers[i]
            for j in range(i+1, len(numbers)):
                if numbers[j] == difference:
                    return [i+1,j+1]
print(Solution().twoSum([0,0,3,4],0))