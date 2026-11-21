class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # userId: set for fast look up and remove
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))
        if userId not in self.following:
            self.following[userId] = set()

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []

        for i in range(len(self.tweets) - 1, -1, -1):
            tw = self.tweets[i]
            if len(result) == 10:
                break
            
            uid, twid = tw
            if uid == userId or uid in self.following[userId]:
                result.append(twid)

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
