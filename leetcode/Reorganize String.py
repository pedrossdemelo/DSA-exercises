# https://leetcode.com/problems/reorganize-string/

# Time: O(nlogn) | Space: O(n)
from collections import Counter
import heapq

# Time: O(nlogn) | Space: O(n)
def reorganizeString(s):
    maxheap = [(-count, letter) for letter, count in Counter(s).most_common()]
    heapq.heapify(maxheap)
    result = ""
    while maxheap:
        count, letter = heapq.heappop(maxheap)
        count2, letter2 = heapq.heappop(maxheap) if maxheap else (0, "")

        result += letter + letter2
        if letter2 == "":
            break

        if -count > 1:
            heapq.heappush(maxheap, (count + 1, letter))
        if -count2 > 1:
            heapq.heappush(maxheap, (count2 + 1, letter2))
    return result if len(result) == len(s) else ""


print(reorganizeString("zifrfbctby"))
