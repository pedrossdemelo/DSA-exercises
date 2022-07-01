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

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))