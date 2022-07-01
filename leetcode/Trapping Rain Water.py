# https://leetcode.com/problems/trapping-rain-water/

# Time: O(n) | Space: O(n)
def trap(height):
    n = len(height)
    trapped = height.copy()
    tallesti = 0
    for l in range(n):
        if trapped[tallesti] <= trapped[l]:
            trapped[tallesti+1:l] = [trapped[tallesti]] * (l-tallesti-1)
            tallesti = l
    tallesti = n-1
    for r in range(n-1,-1,-1):
        if trapped[tallesti] <= trapped[r]:
            trapped[r+1:tallesti] = [trapped[tallesti]] * (tallesti-r-1)
            tallesti = r
    return sum(water - h for water, h in zip(trapped, height))


# Time: O(n) | Space: O(1)
def trap(h):
    n, water = len(h), 0
    left, right = 0, n-1
    lmax, rmax = h[left], h[right]

    while left < right:
        if rmax < lmax:
            right -= 1
            hright = h[right]
            rmax = max(rmax, hright)
            water += max(min(rmax,lmax) - hright, 0)
        else:
            left += 1
            hleft = h[left]
            lmax = max(lmax, hleft)
            water += max(min(rmax,lmax) - hleft, 0)

    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))