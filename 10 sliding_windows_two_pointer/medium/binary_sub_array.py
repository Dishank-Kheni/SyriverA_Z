def numSubarraysWithSum(nums, goal):
    n = len(nums)
    ans = 0

    for i in range(n):
        tmp, l = 0, i

        for r in range(i, n):
            tmp += nums[r]
            if tmp == goal:
                ans += 1
            if tmp > goal:
                break

    return ans


print(numSubarraysWithSum([1, 0, 1, 0, 1], 2))
print(numSubarraysWithSum([0, 0, 0, 0, 0], 0))
