class ATM:
    def __init__(self):
        self.banknotesCount=[20,50,100,200,500]
        self.money=[0,0,0,0,0]
    def deposit(self, banknotesCount: List[int]) -> None:
        for i,j in enumerate(banknotesCount):
            self.money[i]+=j
    def withdraw(self, amount: int) -> List[int]:
        money=[]
        for i in range(4,-1,-1):
            print(i,money,amount)
            if amount<self.banknotesCount[i]:
                money.append(0)
                continue
            if self.money[i]>=amount//self.banknotesCount[i]:
                print(amount)
                money.append(amount//self.banknotesCount[i])
                amount-=amount//self.banknotesCount[i] *self.banknotesCount[i]
            else:
                money.append(self.money[i])
                amount-=self.money[i]*self.banknotesCount[i]

        if amount==0:
            for i,j in enumerate(money[::-1]):
                self.money[i]-=j
            return money[::-1]
        return [-1]

            
           