class Solution:

    words = []

    def encode(self, strs: List[str]) -> str:
        self.words = [s for s in strs]
        print("WORDS:", self.words)
        stringa = " ".join(s for s in strs)
        return stringa


    def decode(self, s: str) -> List[str]:
        return self.words

    
