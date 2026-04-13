from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        lhand = len(hand)
        if lhand % groupSize:
            return False
        
        freqs = Counter(hand)

        for val in sorted(freqs):
            curr_freq = freqs[val]

            if curr_freq > 0:
                for i in range(val, val+groupSize):
                    if freqs[i] < curr_freq:
                        return False
                    
                    freqs[i] -= curr_freq
        return True

        