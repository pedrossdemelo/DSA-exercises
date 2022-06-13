# https://leetcode.com/problems/subsets/


# Time: O(2^n) | Space: O(n)
def subsets(nums):
    result, picks = [], []

    def dfs(i):
        if i == len(nums):
            return result.append(picks.copy())
        dfs(i + 1)
        picks.append(nums[i])
        dfs(i + 1)
        picks.pop()

    dfs(0)
    return result


# Time: O(n^2) | Space: O(1)
def subsets(nums):
    results = [[]]
    for num in nums:
        results.extend([res + [num] for res in results])
    return results


print(subsets([1, 2, 3]))
