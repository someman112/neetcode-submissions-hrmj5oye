class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_x = found_y = found_z = False

        for a,b,c in triplets:

            if a > target[0] or b > target[1] or c > target[2]:
                continue

            if a == target[0]:
                found_x = True
            if b == target[1]:
                found_y = True
            if c == target[2]:
                found_z = True
                
            if found_x and found_y and found_z:
                return True
        return False
        