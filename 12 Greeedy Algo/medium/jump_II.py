def canJump(nums):
    nextJump, currentJump, count = 0, 0, 0

    for i in range(len(nums)):
        nextJump = max(nextJump, i+nums[i])
        if i == currentJump:
            count += 1
            currentJump = nextJump

    return count
