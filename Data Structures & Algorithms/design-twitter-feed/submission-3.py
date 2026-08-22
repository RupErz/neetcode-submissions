class Twitter:

    def __init__(self):
        # map each user to a set of follewee
        self.userInfo = defaultdict(set)

        # map each user to a list of their posts
        self.userPost = defaultdict(list) 

        # Having a global timestamp to count recent val each time addPost
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPost[userId].append([self.count, tweetId])
        self.count -= 1 # Since we will use MaxHeap
        # 0, -1, -2, -3, -4
 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Showing current user post -> jsut follow themselve
        self.userInfo[userId].add(userId)

        # Looping through the list of followee of User
        for followeeId in self.userInfo[userId] :
            if len(self.userPost[followeeId]) > 0 :
                # Take the last index of the userId Post
                index = len(self.userPost[followeeId]) - 1
                # Cause we take the most recent post which is lastIndex
                count, tweetId = self.userPost[followeeId][index]
                # count, tweetId, userId and the next recent most post of them.
                minHeap.append([count, tweetId, followeeId, index - 1])
        
        # [1 ,2 ,3] [4, 5]
        # [3, 5] -> [5, 3] -> [4, 3] -> [3] [3 ,2]

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10 :
            # Pop the most recent post 
            count, tweetId , followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0 :
                count, tweetId = self.userPost[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
            
    def follow(self, followerId: int, followeeId: int) -> None:
        # No need to check exist since we use 'defaultdict'
        self.userInfo[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Check if they actually follow that person or not
        if followeeId in self.userInfo[followerId] :
            self.userInfo[followerId].remove(followeeId)
        
