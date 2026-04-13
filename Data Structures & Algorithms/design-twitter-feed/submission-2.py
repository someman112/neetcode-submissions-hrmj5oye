class User:
    def __init__(self, id):
        self.id = id
        self.tweets = []
        self.following = set()


class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0    

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)

        self.users[userId].tweets.append((-self.time, tweetId))
        self.time+=1 

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        
        user = self.users[userId]
        heap = []

        heap.extend(user.tweets[-10:])
        for f in user.following:
            heap.extend(self.users[f].tweets[-10:])
        
        heapq.heapify(heap)
        result = []
        while heap and len(result) < 10:
            result.append(heapq.heappop(heap)[1])
        
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        if followeeId != followerId:
            self.users[followerId].following.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users or followeeId not in self.users:
            return

        if followeeId in self.users[followerId].following:
            self.users[followerId].following.remove(followeeId)
        

