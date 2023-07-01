from collections import deque
from queue import LifoQueue


def next_greater_element(num1, num2):
    st = deque()
    res = {}

    for i in range(len(num2)-1, -1, -1):

        while st and st[-1] <= num2[i]:
            st.pop()

        if st:
            res[num2[i]] = st[-1]
        else:
            res[num2[i]] = -1
        # print(st, end=" ")
        st.append(num2[i])
        # print(st)

        # for index in range(num1):

    return [res[each] for each in num1]


if __name__ == "__main__":
    # print(next_greater_element([5, 7, 1, 2, 6, 0], [1]))
    print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
