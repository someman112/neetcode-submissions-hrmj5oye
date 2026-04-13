class MinStack:

    def __init__(self):
        self.lst = []
        self.minorder = []
        

    def push(self, val: int) -> None:
        self.lst.append(val)
        if not self.minorder or val <= self.minorder[-1]:
            self.minorder.append(val)
        

    def pop(self) -> None:
        if self.lst:
            itm = self.lst.pop()
            if itm == self.minorder[-1]:
                self.minorder.pop()


    def top(self) -> int:
        return self.lst[-1] if self.lst else None
        

    def getMin(self) -> int:
        return self.minorder[-1] if self.minorder else None
