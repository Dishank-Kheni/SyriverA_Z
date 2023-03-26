def selection_sort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

    # for i in range((len(a)-1)):
    #     k = i,
    #     for j in range(i, len(a), 1):
    #         if a[i] < a[k]:
    #             k = j
    #     a[i], a[k] = a[k], a[i]
    # return a

    return a


a = [8, 5, 7, 3, 2]
print(selection_sort(a))
