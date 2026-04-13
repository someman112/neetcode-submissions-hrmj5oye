class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z = -1, -1, -1
        mt = max(target)

        for t in triplets:
            if max(t)<= mt:
                if x < t[0] <= target[0]:
                    x = t[0]

                if y < t[1] <= target[1]:
                    y = t[1]

                if z < t[2] <= target[2]:
                    z = t[2]

        
        return [x,y,z] == target
        