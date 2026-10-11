class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def checkPal(s):
            return s == s[::-1]

        def recur(temp, i, cur):
            #temp: current list of pal substring
            #curr is the current subtring

            #good condition, reached end of string
            if i >= n:
                if not cur: #all substring were inserted -> GOOD CASE
                    #add the whoe list of substring to the res list
                    res.append(temp)
                #bad case, you finished word but did not put all subsrings, backtrack
                return

            #add new char to cur
            cur += s[i]
            #2 choices
            #1 keep growing the substring
            #2 check if it is pal and cut

            #case1
            recur(temp, i+1, cur)

            #case2
            if checkPal(cur):
                #cut the substring, add it to temp and start recursion with a new substring (empty)
                recur(temp + [cur], i+1, "")

        recur([], 0, "")
        return res

            


        