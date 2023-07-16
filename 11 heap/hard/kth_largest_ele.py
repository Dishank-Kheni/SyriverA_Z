import heapq


class kthLargest:
    def __init__(self, k, nums) -> None:
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        # print(self.nums)

    def add(self, val):
        # print(self.nums)
        heapq.heappush(self.nums, val)
        # if len(self.nums) > self.k:
        #     heapq.heappop(self.nums)
        return heapq.nlargest(self.k, self.nums)[-1]


if __name__ == '__main__':
    kL = kthLargest(3, [4, 5, 8, 2])
    print(kL.add(3))   # return 4
    print(kL.add(5))   # return 5
    print(kL.add(10))  # return 5
    print(kL.add(9))   # return 8
    print(kL.add(4))   # return 8
