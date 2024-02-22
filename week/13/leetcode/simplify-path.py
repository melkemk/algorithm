class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i =0 
        t = path.split('/')
        z = []
        for i in t:
            if i:z.append(i)
        t = z
        # t = t.reduce(key = lambda x :x=='/')
        for i in range(len(t)):
            if t[i] =='..':
                if stack:stack.pop()
            elif t[i] !='.':
                stack.append(t[i])
        return '/'+ '/'.join(stack)