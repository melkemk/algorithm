class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        weight = [0]*(len(weights)-1)

        for i in range(len(weights)-1):
            weight[i] = weights[i]+weights[i+1]
        weight.sort()
        print(weight)
        return sum(weight[len(weights)-k:]) - sum(weight[0:k-1])


        