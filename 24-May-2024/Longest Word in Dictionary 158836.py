# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class Solution:

    def insert(self, word: str) -> None:
        start = self.root
        a = ord('a')
        for i,j in enumerate(word):
            if start.children[ord(j)-a]==None:
                start.children[ord(j)-a] = TrieNode()
            start = start.children[ord(j)-a]
        start.is_end = True

    def longestWord(self, words: List[str]) -> str:
        self.root = TrieNode()
        words.sort(key=lambda x:len(x))
        _max = 0 
        ans = []
        if len(words[0])!=1:return ""
        for word in words:
            a = ord('a')
            p = 1 
            start = self.root
            for i in range(len(word)-1):
                if start.children[ord(word[i])-a]:
                    if  not start.children[ord(word[i])-a].is_end:
                        p = 0 
                        break
                    start = start.children[ord(word[i])-a]
                else:
                    p = 0 
                    break  
            if p==1:
                ans.append(word)
                _max  = max(_max,len(word))
                self.insert(word)
        final = []
        for i in ans:
            if len(i)==_max:
                final.append(i)
        return sorted(final)[0]
        
