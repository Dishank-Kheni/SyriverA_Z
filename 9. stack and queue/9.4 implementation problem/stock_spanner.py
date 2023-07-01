
from collections import deque


class StockSpanner:

    def __init__(self) -> None:
        # stock_list = []
        self.st = []
        pass

    def next(self, price):

        # self.stock_list.append(price)
        count = 1
        i = -1
        # st = deque()
        while len(self.st) > 0 and self.st[i] <= price:
            count += 1
            i -= 1

        self.st.append(price)
        print(count)
        return count


if __name__ == "__main__":
    sp = StockSpanner()
    # sp.next()
    sp.next(100)
    sp.next(80)
    sp.next(60)
    sp.next(70)
    sp.next(60)
    sp.next(75)
    sp.next(85)
