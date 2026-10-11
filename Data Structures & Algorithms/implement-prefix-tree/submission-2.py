class TrieNode:
    def __init__(self):
        self.children = {} #hasmap so retrieval of character is O(1)
        self.EOW = False #True if the character in the node ends a word inserted in the Trie

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() #root of trie

    def insert(self, word: str) -> None:
        finalNode = self.root 
        for ch in word:
            if not ch in finalNode.children:
                finalNode.children[ch] = TrieNode()
            #advance
            finalNode = finalNode.children[ch]
        #at the end, mark end of word
        finalNode.EOW = True
        
        
    def common(self, word: str) -> TrieNode | None:
        #since search and startswith differr just for the final EOW handling
        #None if full word not matches (independently of EOW being True/False)
        #otherwise I return the final node
        finalNode = self.root
        for ch in word:
            if not ch in finalNode.children: return None 
            finalNode = finalNode.children[ch]
        return finalNode

    def search(self, word: str) -> bool:
        #search means i have to match all ch of theb word in trie, and last trie node needs to have EOW
        finalNode = self.common(word)
        if not finalNode: return False
        #check EOW
        return finalNode.EOW

        
        

    def startsWith(self, prefix: str) -> bool:
        #like search but without the EOW check
        finalNode = self.common(prefix)
        return finalNode != None
           