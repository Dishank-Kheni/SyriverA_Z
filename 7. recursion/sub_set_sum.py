# subsequnces : a contigious or non-contigious sequence, which follows the order

def fun(i, list, arr):
    if i >= len(arr):

        print(list, sum(list))
        return

    list.append(arr[i])
    fun(i+1, list=list, arr=arr)
    c = []
    # c.__delitem__
    # c.re
    list.remove(arr[i])
    if arr[i] not in list:
        fun(i+1, list=list, arr=arr)


fun(0, [], [1, 2, 2])

# main
# if __name__ == "name":
