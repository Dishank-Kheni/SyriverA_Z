import re


def valid_palidrome(s):

    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    s = s.lower()
    # print(s)
    if len(s) <= 1:
        return True
    else:
        for i in range(0, len(s)//2, 1):
            if s[i] != s[len(s)-i-1]:
                return False
        return True


print(valid_palidrome("A man, a plan, a canal: Panama"))
