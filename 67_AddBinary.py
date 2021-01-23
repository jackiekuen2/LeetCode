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
        result = ""
        i, j, carry = len(a)-1, len(b)-1, 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                sum += ord(b[j]) - ord('0')
                j -= 1
            carry = 1 if sum > 1 else 0 
            result += str(sum % 2)
        if carry != 0:
            result += str(carry)
        return result[::-1]

sol = Solution()

print(sol.addBinary(a = "11", b = "1"))
print(sol.addBinary(a = "1010", b = "1011"))