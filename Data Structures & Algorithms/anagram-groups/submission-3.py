class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.res = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in self.res: self.res[s_sorted] = [s]
            else:
                self.res[s_sorted].append(s)
        return list(self.res.values())

    




        