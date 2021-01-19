class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

sol = Solution()

print(sol.searchInsert(nums=[1,3,5,6], target = 5))
print(sol.searchInsert(nums = [1,3,5,6], target = 2))
print(sol.searchInsert(nums = [1,3,5,6], target = 0))
print(sol.searchInsert(nums = [1,3,5,6], target = 7))
print(sol.searchInsert(nums = [1], target = 0))