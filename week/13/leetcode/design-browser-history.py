class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.place=0
    def visit(self, url: str) -> None:
        self.place+=1
        if len(self.history)==self.place:
            self.history.append(url)
        else:
            self.history=self.history[0:self.place+1]
            self.history[self.place]=url

    def back(self, steps: int) -> str:
        self.place=self.place-steps if self.place-steps>-1 else 0
        return self.history[self.place]

    def forward(self, steps: int) -> str:
        self.place=self.place+steps if self.place+steps<len(self.history) else len(self.history)-1
        return self.history[self.place]


# Your Browserself.history object will be instantiated and called as such:
# obj = Browserself.history(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)