# https://leetcode.com/problems/reduce-array-size-to-the-half/

from collections import Counter


# Time: O(n) | Space: O(n)
def minSetSize(arr):
    n = len(arr)
    removed = result = 0

    for _, count in Counter(arr).most_common():
        removed += count
        result += 1
        if removed >= n // 2:
            break

    return result


arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
print(minSetSize(arr))
