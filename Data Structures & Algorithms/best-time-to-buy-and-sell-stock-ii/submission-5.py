class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        #This works BUT IT IS NOT DP!
        profit = 0
        for day in range(1, len(prices)):
            if prices[day] >= prices[day-1]: profit += prices[day] - prices[day -1]

        return profit
        """

        #DP WAY
        hold = -prices[0] #best profit so far if you end today holding the stock
        #if we start at day 0 it means we bought the stock in the hold case
        free = 0 #best profit so far if you end today holding nothing

        for day in range(1, len(prices)):
            #case A: what happens if i was i end up today holding?
            #case 1: i was already holding
            #case 2: i was free and bought the stock today
            #i wanna maximize hold, so:
            hold = max(hold,free-prices[day])

            #case B: what happens if i end up today free?
            #case 1: i was already free, did not buy
            #case 2: i was holding and sold, takeing profit
            free = max(free, hold+prices[day])

        #i wanna have the maximum profit, so i want to end the final day by being FREE!
        #so i suppose i update the two states in final day, and then return the free state
        return free
        
        