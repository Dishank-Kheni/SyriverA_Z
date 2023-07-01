def characterReplacement(s, k):
    ans = 0
    st = set(s)

    for char in st:
        l = 0
        for r in range(len(s)):
            if s[r] != char:
                if k == 0:
                    while s[l] == char:
                        l += 1
                    l += 1
                else:
                    k -= 1
            ans = max(ans, r-l+1)
    return ans


print(characterReplacement("AABABBA", 1))
print(characterReplacement("ABAB", 2))
