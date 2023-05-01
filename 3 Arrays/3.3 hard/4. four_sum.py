def fourSum(self, nums, target):
    # 4sum to target
    result = []
    nums.sort()
    for a in range(len(nums)-3):
        for b in range(a+1, len(nums)-2):
            c = b+1
            d = len(nums)-1
            while c < d:
                sum = nums[a]+nums[b]+nums[c]+nums[d]
                if sum < target:
                    c += 1
                elif sum > target:
                    d -= 1
                else:
                    if [nums[a], nums[b], nums[c], nums[d]] not in result:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                    while c < d and nums[c] == nums[c+1]:
                        c += 1
                    while c < d and nums[d] == nums[d-1]:
                        d -= 1
                    c += 1
                    d -= 1
    return result
