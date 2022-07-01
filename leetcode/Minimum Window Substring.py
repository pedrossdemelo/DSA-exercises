from collections import Counter

# n = len(s + n) | m = len(t)
# Time: O(n) | Space: O(n + m)
def minWindow(s: str, t: str) -> str:
    start = 0
    lettersneeded = len(t)
    t, counter = Counter(t), Counter()
    minwindow = None
    for end, letter in enumerate(s):
        if letter in t:
            if counter[letter] < t[letter]:
                lettersneeded -= 1
            counter[letter] += 1

        while not lettersneeded:
            if not minwindow or end - start < minwindow[0]:
                minwindow = (end - start, start, end)
            startletter = s[start]
            if startletter in t:
                if counter[startletter] == t[startletter]:
                    lettersneeded += 1
                counter[startletter] -= 1
            start += 1

    return s[minwindow[1]:minwindow[2]+1] if minwindow else ""

s = "ADOBECODEBANC";t = "ABC"
print(minWindow(s, t))