from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # User id --> Followed User id
        self.followers = defaultdict(set)
        # Tweet id --> User id
        self.user_tweets = defaultdict(list)
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user_tweets:
            self.user_tweets[userId] = [(tweetId, self.tweet_count)]
        else:
            if tweetId in self.user_tweets[userId]:
                return
            else:
                self.user_tweets[userId].append((tweetId, self.tweet_count))

        self.tweet_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        list_of_tweets = []

        for id in self.followers[userId]:
            if id in self.user_tweets.keys():
                list_of_tweets += self.user_tweets[id]

        list_of_tweets += self.user_tweets[userId]

        for i in range(1, len(list_of_tweets)):
            key = list_of_tweets[i]

            j = i-1
            while j >= 0 and key[1] > list_of_tweets[j][1]:
                list_of_tweets[j+1] = list_of_tweets[j]
                j -= 1

            list_of_tweets[j+1] = key

        return [x for (x, y) in list_of_tweets][0:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return

        if followerId not in self.followers:
            self.followers[followerId] = set()
            self.followers[followerId].add(followeeId)
        else:
            if followeeId in self.followers[followerId]:
                return
            else:
                self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.followers:
            return
        else:
            if followeeId not in self.followers[followerId]:
                return
            else:
                self.followers[followerId].remove(followeeId)


twitter = Twitter()
twitter.postTweet(1, 5)
twitter.postTweet(1, 13)
twitter.postTweet(1, 101)
twitter.postTweet(1, 505)
twitter.postTweet(1, 1)
twitter.postTweet(1, 2)
twitter.postTweet(1, 5)
twitter.postTweet(1, 12)
twitter.postTweet(1, 22)
twitter.postTweet(1, 29)
twitter.postTweet(1, 9)
print(twitter.getNewsFeed(1))
