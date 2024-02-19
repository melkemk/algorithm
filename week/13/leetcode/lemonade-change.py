class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0 
        tens = 0
        for i in bills:
            print(i)
            if i == 5:
                fives +=1
            if i == 10 :
                if fives :
                    fives -= 1
                    tens += 1
                else : return 0
            if i == 20:
                print(fives,tens)
                if not fives :
                    return 0 
                if fives == 1 and not tens:
                    return 0
                if not tens and fives <3:return 0 
                if tens :
                    tens -= 1
                    fives -= 1
                else :
                    fives -= 3
        return 1
            
