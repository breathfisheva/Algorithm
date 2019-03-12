# numbers = [2,7,11,15], target =17  [1,2]

class Solution:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        num_dict = {}

        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference not in num_dict:
                num_dict






print(Solution().twoSum([0,0,3,4],0))