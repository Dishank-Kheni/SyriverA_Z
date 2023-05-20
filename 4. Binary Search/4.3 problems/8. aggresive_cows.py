def aggresiveCows(stalls, k):
    stalls.sort()

    def distance(min_distance):

        cows = 1
        last_placed_cows = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - last_placed_cows >= min_distance:
                cows += 1
                last_placed_cows = stalls[i]

        return True if cows >= k else False

    left, right = 1, stalls[-1]

    while left <= right:
        mid = (left + right) // 2

        if distance(mid):
            left = mid+1
        else:
            right = mid-1

    return right


# print(aggresiveCows([1, 2, 4, 8, 9], 3))
print(aggresiveCows([10, 1, 2, 7, 5], 3))       
