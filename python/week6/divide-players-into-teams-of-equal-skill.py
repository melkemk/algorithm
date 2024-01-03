class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        x=0
        skill.sort()
        team=skill[0]+ skill[len(skill)-1]
        te=skill[0]* skill[len(skill)-1]
        x=te
        for i in range(1,len(skill)//2):
            if skill[i]+skill[len(skill)-1-i]!=team:
                return -1
            else:x+=skill[i] *skill[len(skill)-1-i]
        return x