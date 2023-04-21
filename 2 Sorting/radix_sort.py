def radixSort(a):
    max_element = max(a)
    digit = len(str(max_element))

    for count in range(digit):
        bins = []
        for _ in range(10):
            bins.append([])

        for each in a:
            # print((each//pow(10, count)) % 10)
            bins[(each//pow(10, count)) % 10].append(each)

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
b = [237, 146, 259, 348, 152, 163, 235, 48, 36, 62]
print(radixSort(b))
