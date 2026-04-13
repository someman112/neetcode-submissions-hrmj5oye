class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks2 = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        tasks2.sort()
        n = len(tasks)
        time = 1
        hp = []
        output = []
        idx = 0

        while len(output) < len(tasks2):
            while idx < n and tasks2[idx][0] <= time:
                enq, proc, i = tasks2[idx]
                heapq.heappush(hp, (proc, i))
                idx+=1
            
            if hp:
                proct,res = heapq.heappop(hp)
                time+=proct
                output.append(res)
            else:
                time = tasks2[idx][0]
        
        return output 