# https://leetcode.com/problems/bitwise-ors-of-subarrays/


# Time: O(n^2) | Space: O(n^2)
def subarrayBitwiseORs(arr):
    ans, vals = set(), set()
    for x in arr: 
        vals = {x | xx for xx in vals} | {x}
        ans |= vals
    return len(ans)

print(subarrayBitwiseORs([1,1,2]))
