class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if not isinstance(x, int):
            raise TypeError("bad input")
        x = str(x)

        result = [x[i] == x[-(i + 1)] for i in range(len(x))]

        for r in result:
            if r == False:
                return r
        else:
            return True

