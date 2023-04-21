def binSort(a):
    max_element = max(a)
    bins = []
    for _ in range(max_element+1):
        bins.append([])

    for ele in a:
        bins[ele].append(ele)

    j = 0

    for each in bins:
        if each == []:
            continue
        else:
            while(len(each) > 0):
                a[j] = each.pop(0)
                j += 1
    return a


a = [6, 8, 3, 10, 15, 6, 9, 12, 6, 3]
print(binSort(a))
