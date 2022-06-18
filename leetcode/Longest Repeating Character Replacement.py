# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import Counter


# Time: O(n) | Space: O(n)
def characterReplacement(s, k):
    start, end = 0, 1
    result = 1
    counter = Counter(s[start:end])
    while end < len(s):
        counter[s[end]] += 1
        end += 1
        if counter.most_common(1)[0][1] + k >= end - start:
            result = max(result, end - start)
        else:
            counter[s[start]] -= 1
            start += 1
    return result

print(characterReplacement("ABAB",1))
