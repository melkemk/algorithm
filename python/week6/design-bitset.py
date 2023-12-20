class Bitset:
    def __init__(self, size: int):
        self.di =[ 0 for i in range(size)]
        self.ones = 0
        self.flipped = False
    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.di[idx] == 1: self.ones += 1
            self.di[idx] = 0
        else:
            if self.di[idx] == 0: self.ones += 1
            self.di[idx] = 1
    
    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.di[idx] == 0: self.ones -= 1
            self.di[idx] = 1
        else: 
            if self.di[idx] == 1: self.ones -= 1
            self.di[idx] = 0
    
    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = len(self.di) - self.ones
    
    def all(self) -> bool:
        return self.ones == len(self.di)
    def one(self) -> bool: 
        return self.ones > 0 
    def count(self) -> int: 
        return self.ones
    def toString(self) -> str: 
        if self.flipped: return ''.join([str(0 if i else 1) for i in self.di])
        return ''.join([str(i) for i in self.di])