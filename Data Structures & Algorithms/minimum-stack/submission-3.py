class MinStack:

    def __init__(self):
        self.lst = []
        self.minorder = []
        self.d = {}
        

    def push(self, val: int) -> None:
        if not self.minorder or self.minorder[-1] > val:
            self.minorder.append(val)



        if val in self.d:
            self.d[val]+=1
        else:
            self.d[val] = 1
            
        self.lst.append(val)
        

    def pop(self) -> None:
        if self.lst:
            itm = self.lst.pop()

            if self.minorder and self.minorder[-1] == itm:
                self.d[itm] -=1
                
                if self.d[itm] == 0:
                    self.minorder.pop()


    def top(self) -> int:
        if self.lst:
            return self.lst[-1]
        
        

    def getMin(self) -> int:
        if self.minorder:
            return self.minorder[-1]

        
