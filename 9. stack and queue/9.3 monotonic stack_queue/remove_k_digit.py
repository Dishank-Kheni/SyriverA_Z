def remove_k_digit(num, k):
    num_list = [int(each) for each in num]
    print(num_list)
    st = []
    # s = ""
    i = 0
    try:
        while k > 0:
            if num_list[i] < num_list[i+1]:
                st.append(num_list.pop(i+1))
                k -= 1
            elif num_list[i] > num_list[i+1]:
                st.append(num_list.pop(i))
                k -= 1
    except:
        print("Error")
    # print(st)
    print(num_list)
    #     pass


if __name__ == "__main__":
    remove_k_digit("1432219", 3)
    remove_k_digit("10200", 1)
    remove_k_digit("10", 2)

    # 1219
    pass
