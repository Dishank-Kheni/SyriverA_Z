def largestOddNumber(num):
    INT_NUM = int(num)

    while INT_NUM > 0:
        if((INT_NUM % 10) % 2) == 0:
            INT_NUM = INT_NUM // 10
        else:
            return str(INT_NUM)

    return ""


print(largestOddNumber("52"))
print(largestOddNumber("4206"))
print(largestOddNumber("35427"))
