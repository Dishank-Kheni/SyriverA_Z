def rotateString(s, goal):

    for _ in range(len(s)):
        if goal == s:
            return True
        goal = goal[-1]+goal[0:-1]
    return False


print(rotateString("abcde", "cdeab"))
print(rotateString("abcde", "abced"))
