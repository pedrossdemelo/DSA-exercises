# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

# n = amount of words, m = average word length
# Time: O(n * m) | Space: O(n)
def groupAnagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        counter = [0] * 26
        for letter in word:
            counter[ord(letter) - ord("a")] += 1
        anagrams[tuple(counter)].append(word)

    return anagrams.values()

# Time: O(n * log(n) * m) | Space: O(n)
def groupAnagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        letters = "".join(sorted(word))
        anagrams[letters].append(word)

    return anagrams.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))
