

# def com_sum(index, target, ans_list, arr, final_sum):

#     if index == len(arr):
#         if target == 0:
#             final_sum.append(ans_list.copy())
#         return
#     if arr[index] <= target:
#         ans_list.append(arr[index])
#         com_sum(index, target - arr[index], ans_list, arr, final_sum)
#         ans_list.pop()
#     com_sum(index+1, target, ans_list, arr, final_sum)


# if __name__ == "__main__":
#     final_sum = []
#     com_sum(0, 7, [], [2, 3, 6, 7], final_sum)
#     print(final_sum)

def com_sum(index, target, ans_list, arr, final_sum):

    if target == 0:
        final_sum.append(ans_list.copy())
        return
    if index >= len(arr) or arr[index] > target:
        return

    ans_list.append(arr[index])
    com_sum(index, target - arr[index], ans_list, arr, final_sum)
    ans_list.pop()
    com_sum(index+1, target, ans_list, arr, final_sum)


if __name__ == "__main__":
    final_sum = []
    com_sum(0, 7, [], [2, 3, 6, 7], final_sum)
    print(final_sum)
