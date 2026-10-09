class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0: return 0
        memo = {}

        def dfs(amount):
            if amount == 0: return 0
            if amount in memo: return memo[amount]

            res = 1e9

            for coin in coins:
                newamount = amount - coin
                if newamount >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res

            return res


        minCoins = dfs(amount)
        if minCoins == 1e9: return -1
        return minCoins


        


        