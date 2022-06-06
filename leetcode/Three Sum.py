# https://leetcode.com/problems/3sum/a

def threeSum(nums):
    nums.sort()
    last = len(nums) - 1
    result = []

    # a, b, c = numbers in composition
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        left, right = i + 1, last

        while left < right:
            b, c = nums[left], nums[right]
            sum = a + b + c
            if sum == 0:
                result.append([a,b,c])
                while last > left and nums[left] == b:
                    left += 1
                while 0 < right and nums[right] == c:
                    right -= 1
            if sum < 0:
                while last > left and nums[left] == b:
                    left += 1
            if sum > 0:
                while 0 < right and nums[right] == c:
                    right -= 1

    return result


print(threeSum([-1,0,1,2,-1,4]))