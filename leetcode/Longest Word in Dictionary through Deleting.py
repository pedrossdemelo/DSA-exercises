# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

# n = len(dictionary) | s = len(s)
# Time: O(ns) | Space: O(s)
def isSubsequence(big, small):
    if len(small) > len(big):
        return False
    if len(small) == len(big):
        return small == big
    big_i = -1
    small_i = 0
    while small_i < len(small):
        big_i = big.find(small[small_i], big_i + 1)
        if big_i < 0:
            return False
        small_i += 1
    return True


def findLongestWord(s, dictionary):
    max = ""
    for word in dictionary:
        if isSubsequence(s, word) and (
            len(word) > len(max) or (len(word) == len(max) and word < max)
        ):
            max = word
    return max


s = "applea"
dictionary = ["ale", "apple", "monkey", "plea"]
print(findLongestWord(s, dictionary))
