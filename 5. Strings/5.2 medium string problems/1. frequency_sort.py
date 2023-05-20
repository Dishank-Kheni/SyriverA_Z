def frequencySort(s):
    dictionairy = {}
    for each in s:
        if dictionairy.get(each) == None:
            dictionairy[each] = 1
        else:
            val = dictionairy.get(each)
            val += 1
            dictionairy[each] = val

    dictionairy = {key: val for key, val in sorted(
        dictionairy.items(), )}
    dictionairy = {key: val for key, val in sorted(
        dictionairy.items(), key=lambda item: item[1], reverse=True)}
    # dictionairy = sorted(dictionairy.items())
    res = ""
    for key, val in dictionairy.items():
        res += key*val

    return res


print(frequencySort("tree"))
print(frequencySort("cccaaa"))
print(frequencySort("Aabb"))
