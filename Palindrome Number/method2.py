class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        return x[:] == x[::-1]

s = Solution()
print(s.isPalindrome(121))