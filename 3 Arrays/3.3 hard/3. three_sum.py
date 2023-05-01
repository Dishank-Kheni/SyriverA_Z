# inspiring

def three_sum(a):
    a.sort()

    result = []
    for i in range(len(a)-2):
        if i > 0 and a[i] == a[i - 1]:
            continue
        l = i+1
        r = len(a)-1

        while l < r:
            sum = a[i] + a[l] + a[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                result.append([a[i], a[l], a[r]])
                while l < r and a[l] == a[l + 1]:
                    l += 1
                while l < r and a[r] == a[r - 1]:
                    r -= 1
                l += 1
                r -= 1

    return result


print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 1, 1]))
