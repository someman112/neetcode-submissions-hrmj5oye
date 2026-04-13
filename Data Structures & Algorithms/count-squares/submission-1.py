class CountSquares:

    def __init__(self):
        self.pts = defaultdict(int)
        self.lst = []
        

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)]+=1
        self.lst.append(tuple(point))
        

    def count(self, point: List[int]) -> int:
        res = 0 
        x,y = point

        for dx, dy in self.lst:
            if abs(x-dx)!=abs(y-dy) or (x,y) == (dx,dy):
                continue 

            res+= self.pts[(x, dy)] * self.pts[(dx, y)] 
        
        return res
        
