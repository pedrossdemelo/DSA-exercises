# https://leetcode.com/problems/word-break/

def wordBreak(s, wordDict):
    wordDict = set(wordDict)

    there_is_a_solution_at = [False] * len(s) + [True]

    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s) + 1):
            if there_is_a_solution_at[j] and s[i:j] in wordDict:
                there_is_a_solution_at[i] = True
                continue

    return there_is_a_solution_at[0]


print(wordBreak("a" * 10000, ["a" * n for n in range(100)]))
