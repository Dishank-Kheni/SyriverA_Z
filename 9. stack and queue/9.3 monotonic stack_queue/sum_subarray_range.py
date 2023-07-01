res = []


def fun(i, list, arr):
    if i >= len(arr):
        res.append(list.copy())
        return

    list.append(arr[i])
    # res.append([arr[i]])
    fun(i+1, list, arr)

    for j in range(len(arr)-i+1):
        fun(len(arr), arr[j:j+i], arr)

    # list.remove(arr[i])
    # fun(i+1, list, arr)hfbldiufhgduhfg

    # for i

# def fun1(i,list,arr):
#     if i<= len(arr):
#         print(list)
#         return

#     for j in range(len(arr)):


if __name__ == "__main__":
    arr = [1, 2, 3]
    arr = [1, 3, 3]
    arr = [4, -2, -3, 4, 1]
    # arr = [1, 2, 3, 4, 5]
    # arr = [11, 81, 94, 43, 3]
    fun(0, [], arr)
    sum = 0
    for each in res:
        if each != [] and len(each) > 1:
            sum += (max(each) - min(each))
    print(res)
    print(sum)
