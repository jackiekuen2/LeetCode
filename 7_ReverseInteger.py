class Solution:
    def reverse(self, x: int) -> int:
        revs_number = 0
        if x > 0:
            number = abs(x)
            while number > 0:
                remainder = number % 10
                revs_number = (revs_number * 10) + remainder
                number = number // 10
            return revs_number if -pow(2, 31) <= revs_number <= pow(2, 31)-1 else 0
        else:
            number = abs(x)
            while number > 0:
                remainder = number % 10
                revs_number = (revs_number * 10) + remainder
                number = number // 10
            return -revs_number if -pow(2, 31) <= -revs_number <= pow(2, 31)-1 else 0


sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-987))
print(sol.reverse(1534236469))