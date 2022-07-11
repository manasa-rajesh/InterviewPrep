class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for ele in word:
            if ele not in cur.child:
                cur.child[ele] = TrieNode()
            cur = cur.child[ele]
        cur.end = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for ele in word:
            if ele in cur.child:
                cur = cur.child[ele]
            else:
                return False
        if cur.end:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ele in prefix:
            if ele in cur.child:
                cur = cur.child[ele]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)