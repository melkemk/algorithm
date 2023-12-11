class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content={}
        for path in paths:
            p=path.split()
            xx=p[1:]
            dir=p[0]+'/'
            for x in xx:
                con=x.split('(')[1][:-1]
                main=x.split('(')[0]
                if con in content:
                    content[con].append(dir + main)
                else:
                    content[con] = [dir + main]
        a=(i for i in  content.values() if len(i)>1)
        return a
