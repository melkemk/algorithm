# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
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
        def dfs(j,start):
            if j == len(word):return start.is_end 
            if word[j]=='.':
                for i in range(26):
                    if start.children[i]:
                        if dfs(j+1,start.children[i]):return 1 
                # if dfs(j+1,start):return 1 
            elif start.children[ord(word[j]) - 97]:
                return dfs(j+1,start.children[ord(word[j]) - 97] )
            return 0 

        return dfs(0,start)
            
        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)