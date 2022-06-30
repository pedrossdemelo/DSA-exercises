# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

# Time: O(n) | Space: O(n)
def lengthOfLongestSubstring(s: str) -> int:
    lastseen = {}
    maxlen = start = 0
    for i, letter in enumerate(s):
        if letter in lastseen and lastseen[letter] >= start:
            start = lastseen[letter] + 1
        else:
            maxlen = max(maxlen, 1 + i - start)
        lastseen[letter] = i
    return maxlen


print(lengthOfLongestSubstring("dvdf"))
