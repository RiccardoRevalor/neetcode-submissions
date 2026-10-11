class TrieNode:
    def __init__(self):
        self.index = -1 #index of the word we add to theb trie,, so we just add the word to final res one
        self.characters = {}
        self.EOW = False

class Trie:

    def __init__(self):
        self.root = TrieNode() #root of trie

    def insert(self, word: str, index: int) -> None:
        finalNode = self.root 
        for ch in word:
            if not ch in finalNode.characters:
                finalNode.characters[ch] = TrieNode()
            #advance
            finalNode = finalNode.characters[ch]
        #at the end, mark end of word
        finalNode.EOW = True
        #and we assign the index
        finalNode.index = index

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        res = [] #list of matched words in grid
        trie = Trie()
        #1 insert all words in trie
        for i in range(len(words)): trie.insert(words[i], i)

        def recur(i,j, board, currNode):
            #for each char in grid, search if it exists in ucrrent trie node
            #bad case: out of bounds
            if i < 0 or j < 0 or i >= ROWS or j >= COLS:
                return
            #bad case: current cell does not exist in trie node,, prune 
            ch = board[i][j]
            if not ch in currNode.characters: return 
            #good case, it exists and we reached EOW
            currNode = currNode.characters[ch]
            if currNode.EOW and currNode.index >= 0:
                #make sure we just insert the word once
                res.append(words[currNode.index])
                currNode.index = -1
                
            
            #else: ch matched but we still are not at the end of the word
            #continue recurring witb next cells, avoid impossible cases
            #avoid revisiting the same cell
            board[i][j] = "$" #it means already visited, to avoid infinite looping
            recur(i+1, j, board, currNode)
            recur(i, j+1, board, currNode)
            recur(i-1, j, board, currNode)
            recur(i, j-1, board, currNode)
            #restore
            board[i][j] = ch

        #pick each cell as the start of a board
        for i in range(ROWS):
            for j in range(COLS):
                recur(i, j, board, trie.root)
        return res




        