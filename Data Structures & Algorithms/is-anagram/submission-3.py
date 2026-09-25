class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.occ1 = {}
        self.occ2 = {}
        for ch in s:
            if not ch in self.occ1: self.occ1[ch] = 1
            else: self.occ1[ch] +=1
        for ch2 in t:
            if not ch2 in self.occ2: self.occ2[ch2] = 1
            else: self.occ2[ch2] += 1
        for key in self.occ1:
            if key not in self.occ2: return False
            if self.occ1[key] != self.occ2[key]: return False
        for key2 in self.occ2:
            if key2 not in self.occ1: return False
            if self.occ1[key2] != self.occ2[key2]: return False

        return True

        