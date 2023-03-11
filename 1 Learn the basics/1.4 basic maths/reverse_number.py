def reverse_num(n):
    neg = False
    if n < 0:
        n = -n
        neg = True
    rev = 0
    while n > 0:
        rev = rev*10 + n % 10
        n = n//10
    return -rev if neg else rev


n = -123450
print(reverse_num(n))
