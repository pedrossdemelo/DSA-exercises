# https://leetcode.com/problems/solving-questions-with-brainpower/

# Time: O(n) | Space: O(n)
def mostPoints(questions):
    n = len(questions)
    best_starting_at = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        points, brainpower = questions[i]
        score_if_answer = points + best_starting_at[min(n, i + 1 + brainpower)]
        score_if_skip = best_starting_at[min(n, i + 1)]
        best_starting_at[i] = max(score_if_answer, score_if_skip)
    return best_starting_at[0]


questions = [[3,2],[4,3],[4,4],[2,5]]
print(mostPoints(questions))