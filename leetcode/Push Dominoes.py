# https://leetcode.com/problems/push-dominoes/

# Time: O(n) | Space: O(1)
def pushDominoes(dominoes):
    n = len(dominoes)
    result = list(dominoes)
    nextRight = [i for i in range(n) if dominoes[i] == "R"] + [n]
    nextLeft = [i for i in range(n - 1, -1, -1) if dominoes[i] == "L"] + [-1]

    for i in range(len(nextLeft) - 1):
        l, lnext = nextLeft[i], nextLeft[i + 1]
        while r >= -len(nextRight) and nextRight[r] > l:
            r -= 1
        if r >= -len(nextRight) and lnext < nextRight[r] < l:
            topple = (l - nextRight[r] - 1) // 2
            result[l - topple : l] = "L" * topple
        else:
            topple = l - max(lnext, 0)
            result[max(lnext, 0) : l] = "L" * topple

    l = -1
    for i in range(len(nextRight) - 1):
        r, rnext = nextRight[i], nextRight[i + 1]
        while l >= -len(nextLeft) and nextLeft[l] < r:
            l -= 1
        if l >= -len(nextLeft) and rnext > nextLeft[l] > r:
            topple = (nextLeft[l] - r - 1) // 2
            result[r + 1 : r + topple + 1] = "R" * topple
        else:
            topple = min(rnext, n - 1) - r
            result[r + 1 : min(rnext, n - 1) + 1] = "R" * topple

    return "".join(result)


dominoes = ".L.R...L...L.."
print(pushDominoes(dominoes))
