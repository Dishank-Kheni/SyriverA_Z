def fun(i, list, arr, sum, k):
    if i >= len(arr):
        if sum == k:
            print(list)
        return

    sum += arr[i]
    list.append(arr[i])
    fun(i+1, list=list, arr=arr, sum=sum, k=k)
    # c = []
    # c.__delitem__
    # sum -= arr[i]
    sum -= list.pop()
    fun(i+1, list=list, arr=arr, sum=sum, k=k)


fun(0, [], [1, 2, 1], 0, 2)
