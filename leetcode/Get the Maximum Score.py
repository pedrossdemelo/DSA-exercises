from bisect import bisect_left
from itertools import accumulate

# Time: O(n) | Space: O(n)
def maxSum(nums1, nums2):
    accu1, accu2, portals = [0, *accumulate(nums1)], [0, *accumulate(nums2)], [(1,1)]
    result = i1 = i2 = 0
    while i1 < len(nums1) and i2 < len(nums2):
        if nums1[i1] > nums2[i2]:
            i2 = bisect_left(nums2, nums1[i1], lo=i2)
        elif nums1[i1] < nums2[i2]:
            i1 = bisect_left(nums1, nums2[i2], lo=i1)
        elif nums1[i1] == nums2[i2]:
            portals.append((i1+1, i2+1))
            i1 += 1
            i2 += 1

    portals.append((len(accu1), len(accu2)))
    for i in range(len(portals) - 1):
        (i1, i2), (i1next, i2next) = portals[i], portals[i+1]
        best_path = max(accu1[i1next-1] - accu1[i1-1], accu2[i2next-1] - accu2[i2-1])
        result += best_path

    return result % (10**9 + 7)


nums1 = [2,4,5,8,10]; nums2 = [4,6,8,9]
nums1, nums2 = (
[1,2,3,4,5],
[6,7,8,9,10]
)
print(maxSum(nums1, nums2))
