def isAnagram(s, t):
    count = count1 = 0
    for each in s:
        count += ord(each)
    for each in t:
        count1 += ord(each)

    return count == count1


print(isAnagram("anagram", "nagaram"))

print(isAnagram("rat", "car"))
