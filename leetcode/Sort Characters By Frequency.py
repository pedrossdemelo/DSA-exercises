# https://leetcode.com/problems/sort-characters-by-frequency/
from collections import Counter

# Time: O(n) | Space: O(n)
def frequencyStart(s):
    result = ""
    for letter, count in Counter(s).most_common():
        result += letter * count
    return result


s = "bbAaccaac"
print(frequencyStart(s))
