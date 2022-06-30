# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Time: O(n) | Space: O(1)
def removeDuplicates(nums):
    start = end = 0
    while end < len(nums):
        while end < len(nums) and nums[end] == nums[start]:
            end += 1
        if end - start > 2:
            nums[start:end] = [nums[start]] * 2
            start = end = start + 2
        else:
            start = end


nums = [0,0,1,1,1,1,2,3,3]
removeDuplicates(nums)
print(nums)
