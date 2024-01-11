class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set(list(('a', 'e', 'i', 'o', 'u')))
        each=0
        for i in range(k):
            if s[i] in vowels:each+=1
        _max=each
        for i in range((k),len(s)):
            if s[i] in vowels:each+=1
            if s[i-k] in vowels:each-=1
            _max=max(each,_max)
        return _max

