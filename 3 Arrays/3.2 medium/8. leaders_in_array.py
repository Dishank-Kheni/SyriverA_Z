def leaders_in_array(a):
    greater = -1
    leaders = []

    for i in range(len(a)-1, -1, -1):
        if a[i] > greater:
            leaders.append(a[i])
            greater = a[i]

    return leaders


print(leaders_in_array([4, 7, 1, 0]))
print(leaders_in_array([10, 22, 12, 3, 0, 6]))
