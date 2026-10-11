class TrieNode:
    def __init__(self):
        self.EOW = False
        self.characters = {} #hashmap so O(1) retrieval

class WordDictionary:

    def __init__(self):
        #this is a trie + jolly (done with recursion)
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        #addword is standard trie addition
        finalNode = self.root
        for ch in word:
            if not ch in finalNode.characters:
                finalNode.characters[ch] = TrieNode()
            finalNode = finalNode.characters[ch]
        #set EOW
        finalNode.EOW = True
        

    def search(self, word: str) -> bool:
        #. is a jolly ch
        #i need to recursively check all trees
        n = len(word)

        def recur(pos, finalNode) -> bool:
            #pos: index of word that i am currently searching in trie
            #finalNode: current node i'm looking into

            #good case: full word matched
            #bad case: full word but EOW is false
            if pos == n:
                return finalNode.EOW
            

            #2 cases:
            #1. character is a normal letter, just do plain matching and return False if mathing fails, pruning
            ch = word[pos]
            if ch != '.':
                if not ch in finalNode.characters: return False
                # else: continue 
                return recur(pos +1, finalNode.characters[ch])
            else:
                #ch is jolly, try all existing tries
                for trie in finalNode.characters:
                    #select each trie and recur
                    #pruning, onsce i found a trie that leads to solution, no sense in checking all others
                    if recur(pos+1, finalNode.characters[trie]): return True

                return False

        return recur(0, self.root)
                

            
        
