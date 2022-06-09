# https://leetcode.com/problems/generate-parentheses/

# Time: O(?) | Space: O(?)
def generateParenthesis(n):
    results = []
    iterations = 0
    def dfs(string, p_left, p_open):
        nonlocal iterations
        iterations += 1
        if p_left == 0:
            results.append(string + ")" * p_open)
            return
        dfs(string + "(", p_left - 1, p_open + 1)
        if p_open > 0:
            dfs(string + ")", p_left, p_open - 1)

    dfs("(", n - 1, 1)
    return len(results), iterations

print(generateParenthesis(17))