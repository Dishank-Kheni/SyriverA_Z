# subsequnces : a contigious or non-contigious sequence, which follows the order
res = []


def fun(i, list, arr, res):
    if i >= len(arr):
        res.append(list.copy())
        return

    list.append(arr[i])
    fun(i+1, list=list, arr=arr, res=res)
    c = []
    # c.__delitem__
    # c.re
    list.remove(arr[i])
    fun(i+1, list=list, arr=arr, res=res)


if __name__ == "__main__":
    # res = []
    fun(0, [], [3, 1, 2, 4], res)
    print(res)
# main
# if __name__ == "name":
