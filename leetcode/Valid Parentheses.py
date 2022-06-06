# https://leetcode.com/problems/valid-parenthesis/

def isValid(s):
    stack = []

    for char in s:
        match char:
            case "(":
                stack.append(1)
            case ")":
                if len(stack) > 0 and stack[-1] == 1:
                    stack.pop()
                else:
                    return False
            case "{":
                stack.append(2)
            case "}":
                if len(stack) > 0 and stack[-1] == 2:
                    stack.pop()
                else:
                    return False
            case "[":
                stack.append(3)
            case "]":
                if len(stack) > 0 and stack[-1] == 3:
                    stack.pop()
                else:
                    return False

    return True if len(stack) == 0 else False

print(isValid('(()){}[]{{}}[[]]'))