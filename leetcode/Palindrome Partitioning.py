# https://leetcode.com/problems/palindrome-partitioning/

def is_palindrome(s):
    if not s: return False
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Time: O(n * 2^n) | Space: O(n)
def partition(s):
    result, pals = [], []
    def dfs(word, i):
        if i == len(s):
            if not word: result.append(pals.copy())
            return
        word += s[i]
        if is_palindrome(word):
            pals.append(word)
            dfs("", i + 1)
            pals.pop()
        dfs(word, i + 1)
    dfs("", 0)
    return result

print(partition("acaaca"))
