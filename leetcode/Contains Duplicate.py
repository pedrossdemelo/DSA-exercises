# https://leetcode.com/problems/contains-duplicate/

# Time: O(n) | Space: O(n)
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)

    return False

# Time: O(n * log(n)) | Space: O(1)
def containsDuplicate2(nums):
    nums.sort()
    prev_num = None

    for num in nums:
        if num == prev_num:
            return True
        else:
            prev_num = num

    return False
