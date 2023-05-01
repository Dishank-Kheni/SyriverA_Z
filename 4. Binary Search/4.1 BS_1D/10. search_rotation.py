def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) >> 1
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target and nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2, 3], 3))
