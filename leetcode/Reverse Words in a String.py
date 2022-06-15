# https://leetcode.com/problems/reverse-words-in-a-string/

# Time: O(n) | Space: O(n)
def reverseWords(s):
    return " ".join(s.split()[::-1])