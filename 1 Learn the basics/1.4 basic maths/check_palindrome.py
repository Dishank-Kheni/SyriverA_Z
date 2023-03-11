def check_palindrome(n):
    if n < 0:
        return False
    rev = 0
    temp = n
    while n != 0:
        rev = rev*10 + n % 10
        n = n//10
    if temp == rev:
        return True
    else:
        return False


n = 121
print(check_palindrome(n))
