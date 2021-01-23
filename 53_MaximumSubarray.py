"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_sum, current_sum = nums[0], -float('inf')
        for num in nums:
            current_sum = max(num, current_sum + num) # Find the max of new start vs. extension
            max_sum = max(max_sum, current_sum) # Update the max sum
        return max_sum

sol = Solution()

print(sol.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray(nums = [-100000]))
print(sol.maxSubArray(nums= []))