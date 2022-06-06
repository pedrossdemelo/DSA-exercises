# https://leetcode.com/problems/longest-valid-parentheses/

def longestValidParentheses(s):
    s = list(s)
    stack = []
    high_score = 0

    for i, p in enumerate(s):
        if p == "(":
            stack.append(i)
        if p == ")":
            stack.pop()
            if not len(stack):
                stack.append(i)
                continue
            high_score = max(high_score, i - stack[-1])

    return high_score


print(longestValidParentheses("((()))))(()))()()()())"))
