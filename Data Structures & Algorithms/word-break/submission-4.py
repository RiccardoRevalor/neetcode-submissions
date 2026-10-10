class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def recur(amount):
            if amount == "": return True
            if amount in memo: return memo[amount]

            for word in wordDict:
                if amount.startswith(word) and recur(amount[len(word):]):
                    memo[amount] = True
                    return True #early exit

            memo[amount] = False
            return False

        return recur(s)
        