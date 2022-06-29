# https://leetcode.com/problems/heaters/
from typing import List

# n = len(houses) | m = len(heaters)
# Time: O(nlogn + mlogm) | Space: O(1)
def findRadius(houses: List[int], heaters: List[int]) -> int:
    heaters.sort()
    heater = 0
    minradius = -float("inf")
    for location in sorted(houses):
        while heater < len(heaters) - 1 and abs(location - heaters[heater]) >= abs(
            location - heaters[heater + 1]
        ):
            heater += 1
        minradius = max(minradius, abs(location - heaters[heater]))
    return minradius


houses, heaters = ([1, 2, 3, 4, 5, 6, 9], [1, 4])
print(findRadius(houses, heaters))
