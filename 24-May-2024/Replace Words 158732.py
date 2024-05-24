# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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



    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.root = TrieNode()

        for i in dictionary:
            self.insert(i)
        ans =  []
        sentence = sentence.split()
        for word in sentence:
            start = self.root
            a = ord('a')
            one = True
            for i in range(len(word)):
                if not start.children[ord(word[i])-a] : 
                    one  = False
                if  start.children[ord(word[i])-a] and one  :
                    if  start.children[ord(word[i])-a].is_end:
                        ans.append(word[:i+1])
                        break
                    start = start.children[ord(word[i])-a]
            else:
                ans.append(word)
        return " ".join(ans)