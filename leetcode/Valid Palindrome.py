# https://leetcode.com/problems/valid-palindrome/

# made with vim, not manually lol
alphanum = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "w", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" }

def isPalindrome(s):
    l, r = 0, len(s) - 1

    while l <= r:
        while s[l].lower() not in alphanum:
            l += 1
        while s[r].lower() not in alphanum:
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
