class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        par=0
        cube=[1]
        i=0
        while(cube[i]<=n):
            i+=1
            cube.append(pow(3,i+1))
        # if n in cube:
        #     return 
        cube.pop()
        cube.insert(1,3)
        print(cube)
        for j in range(len(cube)-1,-1,-1):
            print(j)
            if(par+cube[j]<n):
                par+=cube[j]
            elif(par+cube[j]==n):
                return True
        return False