class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou'
        cache = {} #here i save the results of indexes of the words i already computed
        def isOk(word):
            if len(word) == 0: return False
            return word[0].lower() in vowels and word[-1].lower() in vowels

        res = []

        for index, query in enumerate(queries):
            li = query[0]
            lr = query[1]
            res_index = 0

            for i in range(li, lr+1):
                if i in cache.keys():
                    res_index += cache[i]
                else:                    
                    comp = isOk(words[i])
                    if comp: res_index +=1
                    cache[i] = comp

            res.append(res_index)

        return res

        