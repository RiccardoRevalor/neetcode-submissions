class Twitter:

    def __init__(self):
        #min heap for the most recent thing
        #hashmap for followers, + list
        #hashmap for posted tweets
        #USE SET TO PREVENT INFINITE REPEAT OF FOLLOW, ETC
        self.postedTweets = defaultdict(set) #key: userid, value = [tweet ids]
        self.following = defaultdict(set) #key: userid, values = [user ids]
        self.id = 0 #tweetid global
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #if userId not in self.postedTweets:
        #    self.postedTweets[userId] = [(self.id, tweetId)]
        #else:
        #    self.postedTweets[userId].append((self.id, tweetId))
        self.postedTweets[userId].add((self.id, tweetId))
        self.id +=1
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #min heap
        recent = []
        if userId in self.following:
            for follows in self.following[userId]:
                if follows in self.postedTweets:
                    for postedT in self.postedTweets[follows]:
                        #populate heap
                        heapq.heappush(recent,postedT)

                        if len(recent) > 10:
                            heapq.heappop(recent)

        #add also user's own postedTweets
        if userId in self.postedTweets:
            #do nothing is user never posted
            for mine in self.postedTweets[userId]:
                #populate heap
                heapq.heappush(recent,mine)

                if len(recent) > 10:
                    heapq.heappop(recent)

        return [tweetId for userId_, tweetId in sorted(recent, reverse=True)]


        

    def follow(self, followerId: int, followeeId: int) -> None:
        #if not followerId in self.following:
        #    self.following[followerId] = [followeeId]
        #else: self.following[followerId].append(followeeId)
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
        
