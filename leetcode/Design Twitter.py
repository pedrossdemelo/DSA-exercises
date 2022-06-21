# https://leetcode.com/problems/design-twitter/

from collections import defaultdict, deque
from typing import List


class Twitter:
    def __init__(self):
        self.tweets = defaultdict(lambda: deque(maxlen=10))
        self.tcount = 0
        self.following = defaultdict(set)

    # O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tcount += 1
        self.tweets[userId].appendleft((tweetId, self.tcount))

    # O(nmlognm)
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = [*self.tweets[userId]]
        for user in self.following[userId]:
            feed.extend(self.tweets[user])
        feed.sort(key=lambda x:x[1], reverse=True)
        return [t[0] for t in feed[:10]]

    # O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    # O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)