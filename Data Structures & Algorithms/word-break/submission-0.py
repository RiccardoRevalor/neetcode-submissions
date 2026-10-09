class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}
        def recur(amount):
            #exit condition, amount is None
            if amount == "": return True

            if amount in memo: return memo[amount]

            result = False
            for word in wordDict:
                #result = result or recur(amount.replace(word, ""))
                if amount.startswith(word):
                    result = result or recur(amount[len(word):])

            memo[amount] = result
            return result

        return recur(s)
        