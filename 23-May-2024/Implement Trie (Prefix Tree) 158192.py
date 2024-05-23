# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]



class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        start = self.root
        a = ord('a')
        for i,j in enumerate(word):
            if start.children[ord(j)-a]==None:
                start.children[ord(j)-a] = TrieNode()
            start = start.children[ord(j)-a]
        start.is_end = True        

    def search(self, word: str) -> bool:
        start = self.root
        a = ord('a')
        for i,j in enumerate(word):
            if start.children[ord(j)-a]==None:return 0
            start = start.children[ord(j)-a]
        return start.is_end   

    def startsWith(self, word: str) -> bool:
        start = self.root
        a = ord('a')
        for i,j in enumerate(word):
            if start.children[ord(j)-a]==None:return 0
            start = start.children[ord(j)-a]
        return 1 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)