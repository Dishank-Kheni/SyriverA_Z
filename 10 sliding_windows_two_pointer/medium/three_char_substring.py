def numberOfSubstrings(s):
    ans = 0
    for l in range(len(s)):
        dictionary = {"a": False, "b": False, "c": False}
        for r in range(l, len(s)):
            dictionary[s[r]] = True
            if dictionary["a"] == True and dictionary["b"] == True and dictionary["c"] == True:
                ans += 1
    return ans


print(numberOfSubstrings("abcabc"))
print(numberOfSubstrings("aaacb"))
print(numberOfSubstrings("abc"))
