import heapq


class medianFinder:
    def __init__(self) -> None:
        self.heap = []
        heapq.heapify(self.heap)

    def addNum(self, num):
        heapq.heappush(self.heap, num)

    def findMedian(self):
        # print(self.heap)
        if len(self.heap) % 2 == 0:

            return heapq.nsmallest((len(self.heap)//2), self.heap)[-1] + heapq.nsmallest((len(self.heap)//2)+1, self.heap)[-1] / 2
        else:
            return heapq.nsmallest(len(self.heap)//2, self.heap)[-1]


if __name__ == '__main__':
    mF = medianFinder()
    mF.addNum(1)
    mF.addNum(2)
    mF.addNum(3)
    mF.addNum(4)
    print(mF.findMedian())
    mF.addNum(5)
    # mF.addNum(3)
    print(mF.findMedian())
