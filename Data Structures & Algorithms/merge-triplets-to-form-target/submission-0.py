class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z = [], [], []
        mt = max(target)

        for t in triplets:
            if max(t)<= mt:
                if t[0] <= target[0]:
                    x.append(t[0])

                if t[1] <= target[1]:
                    y.append(t[1])

                if t[2] <= target[2]:
                    z.append(t[2])

        
        return [max(x, default=-1), max(y, default=-1), max(z, default=-1)] == target
        