class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <2:
            return 0

        mx = 0
        profit = 0
        profits = []

        for i in range(len(prices)-1):
            mx = max(prices[i+1:len(prices)])

            profit = mx - prices[i]

            if profit <0:
                profit = 0

            profits.append(profit)
        
        return max(profits)


