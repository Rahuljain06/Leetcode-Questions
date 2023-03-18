class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        self.hist = self.hist[:self.cur+1] + [url]
        print(self.hist)
        self.cur += 1
        print(self.cur)

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        print(self.cur)
        return self.hist[self.cur]


    def forward(self, steps: int) -> str:
        self.cur = min(len(self.hist)-1, self.cur + steps)
        print(self.cur)
        return self.hist[self.cur]
