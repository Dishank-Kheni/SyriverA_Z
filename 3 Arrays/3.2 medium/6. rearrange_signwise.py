def RearrangebySign(a):
    posIndex = 0
    negIndex = 1

    ans = [0]*len(a)

    for i in range(len(a)):
        if a[i] > 0:
            ans[posIndex] = a[i]
            posIndex += 2

        if a[i] < 0:
            ans[negIndex] = a[i]
            negIndex += 2

    return ans


print(RearrangebySign([1, 2, -4, -5]))
