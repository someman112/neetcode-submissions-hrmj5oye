class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        f = max(freq.values())
        m = sum(1 for v in freq.values() if v == f)
        part_count = f - 1
        part_length = n + 1
        min_slots = part_count * part_length + m
        
        return max(min_slots, len(tasks))
        