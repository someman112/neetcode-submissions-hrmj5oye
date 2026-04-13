class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        rooms = [i for i in range(n)]
        room_count = [0] * n
        hp = []

        for start,end in meetings:
            length = end-start

            while hp and hp[0][0]<=start:
                _,room =heapq.heappop(hp)
                heapq.heappush(rooms, room)

            if rooms:
                room = heapq.heappop(rooms)
                heapq.heappush(hp,(end, room))
                room_count[room]+=1
            
            else:
                end2,room = heapq.heappop(hp)
                heapq.heappush(hp,(end2+length, room))
                room_count[room]+=1
        
        return room_count.index(max(room_count))