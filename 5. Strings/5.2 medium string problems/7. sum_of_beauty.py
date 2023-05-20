def beautySum(s):
    sum = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            dictionairy = {}
            for each in range(i, j+1):
                if dictionairy.get(s[each]) == None:
                    dictionairy[s[each]] = 1
                else:
                    val = dictionairy.get(s[each])
                    val += 1
                    dictionairy[s[each]] = val

            temp = sorted(dictionairy.items(),
                          key=lambda item: item[1], reverse=True)

            large = temp[0][1]
            small = temp[-1][1]

            sum += (large-small)

    # print(dictionairy)
    return sum


print(beautySum("abaacc"))
print(beautySum("aabcb"))
print(beautySum("aabcbaa"))
