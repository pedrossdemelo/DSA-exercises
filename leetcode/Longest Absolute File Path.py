# https://leetcode.com/problems/longest-absolute-file-path/

def serialize(string):
    isFile = string.find('.') > 0
    s = string.split('\t')
    depth = len(s)
    string = s[-1]
    return len(string), depth, isFile

# Time: O(n) | Space: O(n)
def lengthLongestPath(input: str) -> int:
    arr = [serialize(string) for string in input.split('\n')]
    result = 0
    stack, currlen = [], 0
    for namelen, depth, isFile in arr:
        if not isFile:
            while len(stack) >= depth:
                currlen -= stack.pop()
            stack.append(namelen)
            currlen += namelen
        else:
            while len(stack) >= depth:
                currlen -= stack.pop()
            result = max(result, currlen + namelen + len(stack))

    return result

input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(lengthLongestPath(input))