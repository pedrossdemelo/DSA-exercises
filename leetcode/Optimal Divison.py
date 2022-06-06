# https://leetcode.com/problems/optimal-division/

def optimalDivision(nums):
    if len(nums) <= 2:
        return "/".join(str(n) for n in nums)
    division = "(" + "/".join(str(n) for n in nums[1:]) + ")"
    return f"{nums[0]}/" + division


print(optimalDivision([10, 100, 10, 10]))
