"""
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_sum = int(a, 2) + int(b, 2)
        return str(bin(int_sum))[2:]

sol = Solution()

print(sol.addBinary(a = "11", b = "1"))