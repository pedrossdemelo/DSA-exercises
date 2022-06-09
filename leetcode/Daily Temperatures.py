# https://leetcode.com/problems/daily-temperatures/

# Time: O(n) | Space: O(n)
def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack:
            top_i, top_temp = stack[-1], temperatures[stack[-1]]
            if temp > top_temp:
                distance = i - top_i
                result[top_i] = distance
                stack.pop()
            else:
                break
        stack.append(i)

    return result

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))
