class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for n1 in nums1:
            if n1 in nums2:
                result.append(n1)
        return list(set(result))


s = Solution()
print(s.intersection([1,2,3],[1,2]))