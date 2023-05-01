def overLappingSubIntervals(a):
    a.sort()
    min_ele = a[0][0]
    max_ele = a[0][1]

    result = []
    for min, max in a:
        if min <= max_ele:
            if max > max_ele:
                max_ele = max
            continue

        result.append([min_ele, max_ele])
        min_ele = min
        max_ele = max

    result.append([min_ele, max_ele])

    return result


print(overLappingSubIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(overLappingSubIntervals([[1, 4], [4, 5]]))
