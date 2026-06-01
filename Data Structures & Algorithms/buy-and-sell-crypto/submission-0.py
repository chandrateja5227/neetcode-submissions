class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        i = 0
        j = i+1

        while j < len(prices):
            if prices[i] > prices[j]:
                i=j
                j+=1
            elif prices[i] <= prices[j]:
                profit = max(profit ,prices[j] -prices[i] )
                j+=1

            
        return profit

        