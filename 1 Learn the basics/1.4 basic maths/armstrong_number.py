def armstrongNumber(number):
    length = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10
    if number == sum:
        return True
    else:
        return False


number = 1634
print(armstrongNumber(number))
