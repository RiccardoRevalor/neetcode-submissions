class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0: return res

        def recur(temp, amount, close, open):
            #amount is 2n and once it reaches 0 ad close == open that is a good solution
            #close and open serve for pruning
            #as soon as i spot that close > open, i can prune the path
            if close > open: return #prune bad path
            if amount < 0: return 
            if amount == 0 and close == open: #good solution
                res.append(temp)
                return


            #2 cases:
            #1: open (
            #2: close )
            recur(temp + '(', amount -1, close, 1 + open)
            recur(temp + ')', amount -1, 1 + close, open)

        recur("", 2*n, 0, 0)
        return res



        