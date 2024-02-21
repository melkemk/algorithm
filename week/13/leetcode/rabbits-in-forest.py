class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = 0 
        for i in counter:
            print(i,counter[i])
            ans += (ceil( counter[i]/(i+1) ) * (i+1))
        return ans
        