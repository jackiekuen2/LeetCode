class Solution:
    def two_sum(self, nums, target):
        complement_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if num not in complement_map:
                # Find the complement of the number, and save its index
                complement_map[complement] = i
            else:
                # If the complement exists in the hashed map, then the answer is found. Return the answer
                return [complement_map[num], i]

sol = Solution()

print(sol.two_sum([2,7,11,15], 9))
print(sol.two_sum([3, 13, 57, 9, 10, 6], 22))