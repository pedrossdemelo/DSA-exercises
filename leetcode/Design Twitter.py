# https://leetcode.com/problems/design-twitter/

from collections import defaultdict, deque
import heapq
from typing import List


class Twitter:
    def __init__(self):
        self.tweets = defaultdict(lambda: deque(maxlen=10))
        self.tcount = 0
        self.following = defaultdict(set)

    # O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tcount += 1
        self.tweets[userId].appendleft((self.tcount, tweetId))

    # n = following
    # O(nlog10)
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for user in self.following[userId] | {userId}:
            for time, tweetid in self.tweets[user]:
                if len(heap) < 10:
                    heapq.heappush(heap, (time, tweetid))
                elif time > heap[0][0]:
                    heapq.heapreplace(heap, (time, tweetid))

        heap.sort(reverse=True)

        return [tweetid for _, tweetid in heap]

    # O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    # O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


methods = [
    "postTweet",
    "getNewsFeed",
    "follow",
    "postTweet",
    "getNewsFeed",
    "unfollow",
    "getNewsFeed",
]
args = [[1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
expected = [None, [5], None, None, [6, 5], None, [5]]

t = Twitter()

for method, arg, expect in zip(methods, args, expected):
    print()
    print(f"expected: {expect} | got: {getattr(t, method)(*arg)}")
