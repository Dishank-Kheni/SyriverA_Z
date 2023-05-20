def removeOuterParentheses(s):
    stack = []
    res = ""
    openCount = 0
    closeCount = 0

    for para in s:

        if len(stack) == 1:
            if para == "(":
                openCount += 1
            if para == ")":
                closeCount += 1

            if closeCount == openCount:
                stack.pop()
                openCount = closeCount = 0
            else:
                res = res + para
        else:
            openCount += 1
            stack.append(para)

    return res


print(removeOuterParentheses("(()())(())"))
print(removeOuterParentheses("(()())(())(()(()))"))
print(removeOuterParentheses("()()"))
