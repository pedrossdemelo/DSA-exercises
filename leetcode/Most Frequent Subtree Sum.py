# https://leetcode.com/problems/most-frequent-subtree-sum/

from collections import defaultdict

# Time: O(n) | Space: O(n)
def findFrequentTreeSum(root):
    counter = defaultdict(int)
    def dfs(root):
        if not root:
            return 0
        leftsum = dfs(root.left)
        rightsum = dfs(root.right)
        subtreesum = root.val + leftsum + rightsum
        counter[subtreesum] += 1
        return subtreesum
    dfs(root)
    maxcount = (0, [])
    for num, count in counter.items():
        if maxcount[0] < count:
            maxcount = (count, [])
        if maxcount[0] == count:
            maxcount[1].append(num)
    return maxcount[1]