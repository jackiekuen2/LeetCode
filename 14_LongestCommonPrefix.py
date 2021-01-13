class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: #if strs is any kind of zero or empty container
            return ""
        shortest = min(strs, key=len) # pick the one with minimum length
        for i, ch in enumerate(shortest): # Loop over every character
            # Check if the positions of charaters match
            for other in strs:
                if other[i] != ch:
                    return shortest[:i] # Until they find the unmatched character, return the last matched common prefix
        return shortest


sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
print(sol.longestCommonPrefix(['abcqejrpoqi', 'abcpiuprqerq', 'abc', 'abcqer']))