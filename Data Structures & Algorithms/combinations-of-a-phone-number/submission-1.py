class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" or digits is None: return []
        mapper = {}
        mapper['2'] = ["a","b","c"]
        mapper['3'] = ["d", "e", "f"]
        mapper['4'] = ["g", "h", "i"]
        mapper['5'] = ["j", "k", "l"]
        mapper['6'] = ["m", "n", "o"]
        mapper['7'] = ["p", "q", "r", "s"]
        mapper['8'] = ["t", "u", "v"]
        mapper['9'] = ["w", "x", "y", "z"]

        res = []
        n = len(digits)

        def recur(i, temp):
            #good end: i == n 
            if i == n:
                #add the temp combination to res
                res.append(temp)
                return

            #for each number you iterate through mappper[number] and simulate recursion with aòò choices
            for letter in mapper[digits[i]]:
                recur(i+1, temp + letter)

        recur(0, "")
        return res

        