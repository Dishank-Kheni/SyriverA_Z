def numberOfSubarrays(nums, k):
    ans = 0
    for i in range(len(nums)):
        tmp_count = 0
        l = i

        for r in range(i, len(nums)):
            if nums[r] % 2 != 0:
                tmp_count += 1

            if tmp_count == k:
                ans += 1

    return ans


print(numberOfSubarrays([1, 1, 2, 1, 1], 3))
print(numberOfSubarrays([2, 4, 6], 1))
print(numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2   ))
