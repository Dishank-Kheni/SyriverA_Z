def longestCommonPrefix(strs):
    strs.sort()
    # print(strs)
    first = strs[0]
    last = strs[-1]
    for i, char in enumerate(first):
        if char != last[i]:
            return first[:i]
    return first


print(longestCommonPrefix(["flower", "flow", "flight"]))

print(longestCommonPrefix(["dog", "racecar", "car"]))
