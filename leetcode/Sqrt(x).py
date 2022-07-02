# https://leetcode.com/problems/sqrtx/

# Time: O(logn) | Space: O(1)
def mySqrt(x):
    low, high = 0, x
    while high - low > 1:
        mid = (low + high) // 2
        squared = mid * mid
        if squared > x:
            high = mid
        elif squared < x:
            low = mid
        elif squared == x:
            return mid
    return low

print(mySqrt(8))