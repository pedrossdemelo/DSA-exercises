# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import Counter
from typing import List

# Time: O(S) | Space: O(min(P, 128))
def findAnagrams(s: str, p: str) -> List[int]:
    S, P = len(s), len(p)
    if P > S: return []
    anagram = Counter(p)
    window = Counter(s[:P])
    result = [0] if window == anagram else []

    for i in range(P, S):
        start = i - P
        window[s[start]] -= 1
        window[s[i]] += 1
        if (window == anagram):
            result.append(start+1)

    return result

s = "cbaebabacd"; p = "ab"

print(findAnagrams(s, p))
print([ord(a) for a in "abcdefgihjklmnopqrstuvxwyz".upper() +  "abcdefgihjklmnopqrstuvxwyz"])