# https://leetcode.com/problems/fair-distribution-of-cookies/


def distributeCookies(cookies, k):
    distribution = [0] * k
    max_dist = float("inf")
    cookies.sort(reverse=True)

    def dfs(i, child_max=0):
        nonlocal max_dist
        if child_max >= max_dist:
            return

        if i == len(cookies):
            max_dist = min(max_dist, child_max)
            return

        for j in range(k):
            distribution[j] += cookies[i]
            dfs(i + 1, max(child_max, distribution[j]))
            distribution[j] -= cookies[i]

    dfs(0)
    return max_dist


cookies = list(range(1, 5))
k = 2

print(distributeCookies(cookies, k))
