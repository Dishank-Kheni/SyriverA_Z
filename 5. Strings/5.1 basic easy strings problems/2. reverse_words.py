def reverseWords(s):

    stack = []
    i = 0
    res = ""
    while(i < len(s)):
        if s[i] == " ":
            i += 1
            continue
        else:
            words = ""
            while i < len(s) and s[i] != " ":
                words += s[i]
                i += 1

            stack.append(words)

    while len(stack) != 0:
        res += stack.pop()+" "

    return res


print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("   a good   example"))
