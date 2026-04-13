class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        num_groups = len(hand) / groupSize
        hand = Counter(hand)

        while num_groups > 0 and hand:
            curr = min(hand)
            for i in range(groupSize):
                if curr in hand:
                    hand[curr]-=1

                    if hand[curr] == 0:
                        del hand[curr]
                    curr+=1
                else:
                    return False

            num_groups-=1
        return True
        