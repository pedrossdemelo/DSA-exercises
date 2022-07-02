# https://leetcode.com/problems/sqrtx/

# Time: O(logn) | Space: O(1)
def peakIndexInMountainArray(arr):
    n = len(arr)
    left, right = 0, n-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid-1] < arr[mid]:
            left = mid
        elif arr[mid] > arr[mid+1]:
            right = mid

arr = [3,9,8,6,4]
print(peakIndexInMountainArray(arr))