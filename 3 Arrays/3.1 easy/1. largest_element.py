def largest_element(a):
    max = 0
    for each in a:
        if each > max:
            max = each

    return max


print(largest_element([2, 5, 1, 0]))
