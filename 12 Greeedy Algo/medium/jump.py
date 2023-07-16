def canJump(nums):
    nextJump, currentJump = 0, 0

    for i in range(len(nums)):
        nextJump = max(nextJump, i+nums[i])
        if i == currentJump:
            currentJump = nextJump

        if currentJump >= len(nums):
            return True

    return False
