# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

# m = max(weights) | s = sum(weights) | n = len(weights)
# Time: O(nlog(s-m)) | Space: O(1)
def shipWithinDays(weights, days):
    maxcap = sum(weights)
    mincap = max(weights)

    def fitsDeadline(cap):
        nonlocal days
        cargo = next = day = 0
        while next < len(weights):
            while next < len(weights) and cargo + weights[next] <= cap:
                cargo += weights[next]
                next += 1
            day += 1
            cargo = 0
            if day > days:
                return False
        return True

    while mincap < maxcap:
        mid = (maxcap + mincap) // 2
        if fitsDeadline(mid):
            maxcap = mid
        else:
            mincap = mid + 1

    return mincap


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(shipWithinDays(weights, days))
