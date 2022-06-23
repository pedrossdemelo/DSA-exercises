# https://leetcode.com/problems/top-k-frequent-words/

from collections import Counter
import heapq

# Time: O(klogn) | Space: O(n)
def topKFrequent(words, k):
    heap = [(-occurrence, word) for word, occurrence in Counter(words).items()] # O(n) + O(n)
    heapq.heapify(heap) # O(n)
    return [heapq.heappop(heap)[1] for _ in range(k)] # O(klogn)


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
print(topKFrequent(words, 4))
