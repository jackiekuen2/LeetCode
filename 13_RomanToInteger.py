class Solution:
    def romanToInt(self, s: str) -> int:
        """
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        """
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        """
        The trick is that the last letter is always added. 
        Except the last one, if one letter is less than its latter one, this letter is subtracted, else added
        e.g. IV, IX, XL, XC, CD, CM
        """
        for i in range(0, len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]] # Always add the last one


sol = Solution()

print(sol.romanToInt("III"))
print(sol.romanToInt("IV"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))


# My version (Wrong! Didn't handle the subtraction part)
        # roman_list = list(s)
        # sumup = 0
        # for i in roman_list:
        #     if i == "I":
        #         sumup += 1
        #     elif i == "V":
        #         sumup += 5
        #     elif i == "X":
        #         sumup += 10
        #     elif i == "L":
        #         sumup += 50
        #     elif i == "C":
        #         sumup += 100
        #     elif i == "D":
        #         sumup += 500
        #     else:
        #         sumup += 1000
        # return sumup