# https://leetcode.com/problems/container-with-most-water/


def maxArea(height):
    left, right, best = 0, len(height) - 1, 0

    while left < right:
        left_h, right_h, distance = height[left], height[right], right - left
        lowest_h = min(left_h, right_h)
        best = max(best, lowest_h * distance)
        if left_h < right_h:
            left += 1
            while left_h < lowest_h:
                left += 1
        else:
            right -= 1
            while right_h < lowest_h:
                right -= 1
    return best

print(maxArea([1, 8, 99, 1, 1, 1, 0, 0, 99, 8, 1]))
