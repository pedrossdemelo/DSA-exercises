from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i, num in enumerate(numbers):
        lookingfor = target - num
        left, right = i + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == lookingfor:
                return i, mid
            elif numbers[mid] > lookingfor:
                right = mid - 1
            else:
                left = mid + 1


