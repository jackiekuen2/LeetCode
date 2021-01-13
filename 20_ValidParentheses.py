class Solution:
    def isValid(self, s: str) -> bool:
        """
        Algorithm 2: 
        - 1. Initialize the stack s = [], and start the loop over the expression from left to right
        - 2. If we encounter an opening bracket, we simply push it onto the stack. 
        - 3. If we encounter a closing bracket, that matches the opening bracket of the same type,. then we pop it off the stack and continue processing.
        - 4. In the end, if we are left with a stack still having elements, then this implies an invalid expression.
        """
        bracket_map = {"(": ")", "{": "}", "[": "]"}
        open_par = set(["(", "{", "["])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif (stack is not None) and i == bracket_map[stack[-1]]: # Verify if stack is not empty
                stack.pop()
            else:
                return False
        return stack == []

    def isValid_1(self, s: str) -> bool:
        """
        Algorithm 1:
        Remove the smaller expressions (i.e. replace with “” empty) one at a time from the overall expression 
        and since this is a valid expression, we would be left with an empty string in the end.

        Cons:
        1. But It's actually O(n^2), which is why it times out. 
        "()" in s is O(n), and you're doing this O(n) times, replace is also an O(n) operation happening O(n) times, 
        implying these steps are both in O(n^2). 

        2. Wouldn't work if there are operators and operands in between brackets.
        """
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}","").replace("[]","")
        return s == ""


sol = Solution()

print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))