"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''.join(map(str, digits))
        res = list(map(int, list(str(int(num)+1))))
        return [0] * (len(digits) - len(res)) + list(res)

sol = Solution()

print(sol.plusOne(digits = [1,2,3]))
print(sol.plusOne(digits = [4,3,2,1]))
print(sol.plusOne(digits = [0]))
print(sol.plusOne(digits = [0, 0]))
print(sol.plusOne(digits = [0, 0, 0]))