"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, 
and only the integer part of the result is returned.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            elif x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1

sol = Solution()

for i in range(10):
    print(sol.mySqrt(i))