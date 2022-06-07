# https://leetcode.com/problems/top-k-frequent-elements/


from collections import Counter


# Time: O(n) | Space: O(n)
def topKFrequent(nums, k):
    count = list(Counter(nums).items())
    count.sort(reverse=True, key=lambda c: c[1])
    return [values[0] for values in count[:k]]


print(topKFrequent([1,1,1,1,1,2,2,2,3,3,0,1,2,3,4,4,4,4,5,5,9,9], 3))
