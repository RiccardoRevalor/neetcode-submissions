class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou'
        def isOk(word):
            if len(word) == 0: return False
            return word[0].lower() in vowels and word[-1].lower() in vowels

        res = []

        for index, query in enumerate(queries):
            li = query[0]
            lr = query[1]
            res_index = 0

            for i in range(li, lr+1):
                if isOk(words[i]): res_index +=1

            res.append(res_index)

        return res

        