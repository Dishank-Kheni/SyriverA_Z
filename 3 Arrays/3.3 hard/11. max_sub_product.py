# inspiring

def maxProductSubArray(num):
    prod1 = prod2 = result = num[0]

    for i in range(1, len(num)):
        prod1 = max(num[i], prod1*num[i], prod2*num[i])
        prod2 = min(num[i], prod1*num[i], prod2*num[i])

        result = max(result, prod1)

    return result


print(maxProductSubArray([1, 2, -3, 0, -4, -5]))
