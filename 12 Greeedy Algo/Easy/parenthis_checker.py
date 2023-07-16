def checkValidString(s):
    leftPara = []
    star = []

    for i in range(len(s)):
        if s[i] == '(':
            leftPara.append(i)
        elif s[i] == '*':
            star.append(i)
        else:
            if len(leftPara) > 0:
                leftPara.pop()
            elif len(star) > 0:
                star.pop()
            else:
                return False

    while len(leftPara) > 0 and len(star) > 0:
        if leftPara.pop() > star.pop():
            return False

    return len(leftPara) == 0
