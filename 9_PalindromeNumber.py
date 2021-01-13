class Solution:
    def isPalindrome(self, x: int) -> bool:
        revs = str(x)[::-1]
        return revs == str(x) if -pow(2, 31) <= x <= pow(2, 31)-1 else 0

sol = Solution()
print(sol.isPalindrome(123))
print(sol.isPalindrome(987654321))
print(sol.isPalindrome(10))
print(sol.isPalindrome(-512))
print(sol.isPalindrome(121))
print(sol.isPalindrome(1234321))