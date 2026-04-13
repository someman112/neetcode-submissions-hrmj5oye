class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for frm,to in tickets:
            adj_list[frm].append(to)
        
        for key in adj_list:
            adj_list[key].sort(reverse=True)
        
        stack = ["JFK"]
        res = []

        while stack:
            if not adj_list[stack[-1]]:
                res.append(stack.pop())
            else:
                stack.append(adj_list[stack[-1]].pop())
        
        res.reverse()
        return res
        