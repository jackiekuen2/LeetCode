class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        '''
        Case 1: if x<0, it means [x<0] will be 1(since it is true) and hence, it would take -1(at 1st index) from [1,-1]
        Case 2: if x>0, it means [x<0] will be 0(since it is false) and hence , it would take 1(at 0th index) from [1,-1]
        '''
        revs_number = 0
        x = abs(x)
        while x > 0:
            remainder = x % 10
            revs_number = (revs_number * 10) + remainder
            x = x // 10
        return sign * revs_number if -pow(2, 31) <= sign * revs_number <= pow(2, 31)-1 else 0

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-987))
print(sol.reverse(1534236469))