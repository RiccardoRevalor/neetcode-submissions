class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        #more optimized version, with prefix sum

        vowels = 'aeiou'
        
        def isOk(word):
            if len(word) == 0: return False
            return word[0].lower() in vowels and word[-1].lower() in vowels

        prefix = [0] * (len(words)+1)

        counter = 0

        for i in range(len(words)):
            if isOk(words[i]):
                prefix[i+1] = counter +1 #i+1 because prefix has one additional ekement at left
                counter +=1
            else:
                prefix[i+1] = counter

        res = []

        for q in queries:
            li = q[0]
            lr = q[1]
            res.append(prefix[lr+1]-prefix[li])

        return res
        
        