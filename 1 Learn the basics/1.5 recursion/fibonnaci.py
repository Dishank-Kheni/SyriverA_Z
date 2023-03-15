

def fibonaaci(n):
    # global sum

    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return fibonaaci(n-1) + fibonaaci(n-2)

    # return sum


print(fibonaaci(8))
