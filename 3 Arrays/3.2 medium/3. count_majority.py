def majorityElement(a):
    min_times = len(a)//2
    max_times = 0
    max_element = 0


    mapp = dict()

    for each in a:
        res= mapp.get(each)
        if res != -1:
            temp_count = a.count(each)
            if temp_count >= min_times:
                if temp_count > max_times:
                    max_times = temp_count
                    max_element = each
            mapp[each] = temp_count
    return max_element


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(majorityElement([4, 4, 2, 4, 3, 4, 4, 3, 2, 4]))
