class Solution:

    """
    #MY OLD SOLUTION
    def find(self, source, ch, start):
        if start == -1: start = 0
        for i in range(start, len(source)):
            if source[i] == ch: return i
        return -1

    def isSubsequence(self, s: str, t: str) -> bool:
        index_s = 0
        index_t = 0
        last = -1
        if len(t) == 0: return False
        if len(s) == 0: return True
        while index_t < len(t):
            ch_s = s[index_s]
            index_t = self.find(t, ch_s, last)
            print("character s:", ch_s)
            print("index_s:", index_s)
            print("index_t:", index_t)
            if index_t == -1 or index_t < last: return False
            index_s +=1
            last = index_t + 1
            if index_s == len(s): return True
        
        return True
    """

    #better one, two pointers style
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 #tracks s
        for ch in t:
            if i < len(s) and s[i] == ch: i += 1
        return i == len(s)


        




        