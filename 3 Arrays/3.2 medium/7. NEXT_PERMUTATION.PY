
result = []


def nextGreaterPermutation(res_perm, remain_perm):
    if len(remain_perm) == 1:
        result.append(res_perm + remain_perm)
        return

    for i in range(len(remain_perm)):

        remain_temp = remain_perm[::]
        result_temp = res_perm[::]
        result_temp.append(remain_perm[i])
        remain_temp.remove(remain_perm[i])
        nextGreaterPermutation(result_temp, remain_temp)


filter(lambda each: each == [2, 1, 3], enumerate(result))
nextGreaterPermutation([], [1, 2, 3])
print(result)
