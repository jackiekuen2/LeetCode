class Solution:
    def maxProfit(self, prices) -> int:
        """
        As long as current price is higher than previous lowest price, max profit could be updated. 
        'min_price' to track previous lowest price (indicating we can buy in that time) and 
        'max_profit' to track max profit we have achieved so far.
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


sol = Solution()

print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))