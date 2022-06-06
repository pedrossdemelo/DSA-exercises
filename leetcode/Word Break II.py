# https://leetcode.com/problems/word-break-ii/


def wordBreak(s, wordDict):
    wordDict = set(wordDict)

    solutions_at = [[] for _ in range(len(s))]
    solutions_at.append([" "])

    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s) + 1):
            if solutions_at[j] and s[i:j] in wordDict:
                solutions_at[i].extend(f" {s[i:j]}" + sol for sol in solutions_at[j])

    return [sol.strip() for sol in solutions_at[0]]


print(wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
