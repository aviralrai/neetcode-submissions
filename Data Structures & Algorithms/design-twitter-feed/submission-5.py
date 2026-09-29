class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.timestamp = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timestamp,tweetId))
        self.timestamp -= 1
    def getNewsFeed(self, userId: int) -> List[int]:
        post = []
        max_heap = []
        for time, postid in self.posts[userId]:
            heapq.heappush(max_heap,(time,postid))
        
        for user in self.follows[userId]:
            if user != userId:
                for time, postid in self.posts[user]:
                    heapq.heappush(max_heap,(time,postid))
        res = []
        while max_heap and len(res) < 10:
            time, pid = heapq.heappop(max_heap)
            res.append(pid)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
