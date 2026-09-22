class Solution:
    def maxProfit(self, prices):

        left = 0
        right = 1
        max_P = 0

        while right < len(prices):
            
            if (prices[left] < prices[right]):
                profit = prices[right] - prices[left]
                max_P = max(max_P, profit)
            else:
                left = right
            right += 1
        
        return max_P
