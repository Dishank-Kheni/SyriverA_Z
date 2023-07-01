def longestOne(nums, k):
    l, ans = 0, 0

    for r in range(len(nums)):
        if nums[r] == 0:
            if k == 0:
                while nums[l] != 0:
                    l += 1
                l += 1
            else:
                k -= 1
        ans = max(ans, r-l+1)

    return ans


print(longestOne([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
