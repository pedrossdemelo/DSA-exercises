# https://leetcode.com/problems/largest-rectangle-in-histogram/

def largestRectangleArea(heights):
    stack = []
    largest = 0
    for i, height in enumerate(heights):
        last_popped_i = None
        while stack and stack[-1][0] > height:
            top_h, top_i = stack.pop()
            last_popped_i = top_i
            distance = i - top_i
            area = distance * top_h
            largest = max(largest, area)
        stack.append((height, last_popped_i if last_popped_i is not None else i))
    while stack:
        top_h, top_i = stack.pop()
        distance = len(heights) - top_i
        area = distance * top_h
        largest = max(largest, area)
    return largest

print(largestRectangleArea([2,1,5,6,2,3]))


