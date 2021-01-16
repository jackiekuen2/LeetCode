class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while True:
            if val not in nums:
                break
            nums.remove(val)
        return len(nums)

sol = Solution()

print(sol.removeElement(nums=[0,1,2,2,3,0,4,2], val=2))
print(sol.removeElement(nums = [3,2,2,3], val = 3))