from collections import deque
from queue import LifoQueue


def next_greater_element(num, ):
    st = deque()
    res = deque()

    for i in range(len(num)-1, -1, -1):

        while st and st[-1] <= num[i]:
            st.pop()

        if st:
            res.appendleft(st[-1])
        else:
            res.appendleft(-1)
        # print(st, end=" ")
        st.append(num[i])
        # print(st)

    # print(st)
    if res[-1] == -1:
        while st:
            temp = st.pop()
            if temp > res[-1]:
                res[-1] = temp
        # for index in range(num1):
    return res


if __name__ == "__main__":
    # print(next_greater_element([5, 7, 1, 2, 6, 0]))
    print(next_greater_element([1, 2, 1]))
    print(next_greater_element([1, 2, 3, 4, 3]))
    # print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))


# 91620100005415

# Tulshibhai arjanbhai kheni

# BOB

# paravdi
