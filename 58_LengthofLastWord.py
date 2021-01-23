"""
Given a string s consists of some words separated by spaces, 
return the length of the last word in the string. If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = s.split()
        return 0 if len(s_list) == 0 else len(s_list[-1])

sol = Solution()

print(sol.lengthOfLastWord(s = "Hello World"))
print(sol.lengthOfLastWord(s = " "))