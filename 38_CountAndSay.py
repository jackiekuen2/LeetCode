"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
which is then converted into a different digit string.
To determine how you "say" a digit string, 
split it into the minimal number of groups so that each group is a contiguous section all of the same character. 
Then for each group, say the number of characters, then say the character. 
To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

Hint 1:
The following are the terms from n=1 to n=10 of the count-and-say sequence:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211

Hint 2:
To generate the nth term, just count and say the n-1th term.
"""
import itertools

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # The first char of our result is 1 so initilize the result
        s = '1'
        for _ in range(n-1):
            s = ''.join(str(len(list(group))) + str(digit) for digit, group in itertools.groupby(s))
            # print(s)
        return s

sol = Solution()

print(sol.countAndSay(3))
print(sol.countAndSay(4))
print(sol.countAndSay(5))