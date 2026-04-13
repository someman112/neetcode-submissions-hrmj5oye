class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = sorted(list((position[i], speed[i]) for i in range(len(speed))))
        arr.reverse()
        

        fleets = []
        for elem in arr:
            time = (target - elem[0]) / elem[1]
            
            if not fleets or fleets[-1] < time:
                fleets.append(time)

        return len(fleets)
        