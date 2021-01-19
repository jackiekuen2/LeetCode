class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


sol = Solution()

print(sol.searchInsert(nums=[1,3,5,6], target = 5))
print(sol.searchInsert(nums = [1,3,5,6], target = 2))
print(sol.searchInsert(nums = [1,3,5,6], target = 0))
print(sol.searchInsert(nums = [1,3,5,6], target = 7))
print(sol.searchInsert(nums = [1], target = 0))