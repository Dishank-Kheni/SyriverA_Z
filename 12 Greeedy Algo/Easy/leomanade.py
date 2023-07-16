def lemonadeChange(bills):

    cash = 0

    for i in range(len(bills)):

        giveBackAmount = bills[i] - 5

        if giveBackAmount > cash:
            return False
        else:
            cash -= giveBackAmount
        cash += 5

    return True


print(lemonadeChange([5, 5, 5, 10, 20]))
print(lemonadeChange([5, 5, 10, 10, 20]))
