# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

from collections import Counter
from functools import reduce
from operator import add


# Time: O(n) | Space: O(n)
def minSteps(s, t):
    c_s, c_t = Counter(s), Counter(t)
    return reduce(add, (c_s - c_t).values(), 0) + reduce(add, (c_t - c_s).values(), 0)


print(minSteps("leetcode", "coats"))
