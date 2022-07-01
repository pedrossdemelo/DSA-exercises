# https://leetcode.com/problems/happy-number/

# Time: O(n) | Space: O(1)
def isHappy(n: int) -> bool:
    def sumsqrt(n):
        return sum(int(num) ** 2 for num in str(n))
    slow = sumsqrt(n)
    fast = sumsqrt(slow)

    while slow != fast and fast != 1:
        slow = sumsqrt(slow)
        fast = sumsqrt(sumsqrt(fast))

    return fast == 1

print(isHappy(2))
