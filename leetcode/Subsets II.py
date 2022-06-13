# https://leetcode.com/problems/subsets-ii/


# Time: O(n^2) | Space: O(n)
def subsetsWithDup(nums):
    nums.sort()
    result, picks = [], []

    def dfs(i):
        result.append(picks.copy())
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]: continue
            picks.append(nums[j])
            dfs(i + 1)
            picks.pop()

    dfs(0)
    return result


nums = [1,2,2]
print(subsetsWithDup(nums))
