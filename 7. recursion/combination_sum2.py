
# learn : Set Using list of list
def com_sum(index, target, ans_list, arr, final_sum):

    if target == 0:
        final_sum.append(tuple(ans_list.copy()))
        return
    if index >= len(arr) or arr[index] > target:
        return

    ans_list.append(arr[index])
    com_sum(index+1, target - arr[index], ans_list, arr, final_sum)
    ans_list.pop()
    if arr[index] not in ans_list:
        com_sum(index+1, target, ans_list, arr, final_sum)


if __name__ == "__main__":
    final_sum = []
    # final_sum = set([(1, 2, 3), (1, 2, 3)])
    # final_sum.add(set([2, 2, 3]))

    arr = [10, 1, 2, 7, 6, 1, 5]
    arr.sort(),
    com_sum(0, 8, [], arr, final_sum)
    print(final_sum)
    # print(list(set(final_sum)))
