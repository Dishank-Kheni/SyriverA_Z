
import heapq
from collections import Counter, defaultdict


# Max heap
class HeapClass:
    def __init__(self, arr=[]):
        # self.heapiFy(arr)
        pass

    def heapiFy(self, arr):
        self.heap = arr
        self.size = len(arr)

        for i in range(self.size//2-1, -1, -1):
            j = 2*i + 1
            while j <= self.size - 1:
                if j < self.size - 1 and self.heap[j] < self.heap[j + 1]:
                    j += 1
                if self.heap[i] < self.heap[j]:
                    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                    i = j
                    j = j * 2
                else:
                    break

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        k = self.size - 1

        while k != 0 and self.heap[k] > self.heap[k//2]:
            self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k = k//2

    def delete(self):
        if self.size == 0:
            return -1
        self.heap[0], self.heap[self.size -
                                1] = self.heap[self.size - 1], self.heap[0]
        self.size -= 1

        i = 0
        j = 1

        while j <= self.size - 1:
            if j < self.size - 1 and self.heap[j] < self.heap[j + 1]:
                j += 1
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                i = j
                j = j * 2
            else:
                break

    def topKFrequent(self, nums):
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1
        self.heapiFy(frequency)
        # print(len(frequency))
        # print(frequency[1])
        for k, v in frequency.items():
            print(k, v)
        print(frequency)
        # heapq.heapify
        cnt = Counter(nums)
        print(cnt)


if __name__ == "__main__":
    # heap = HeapClass([10, 20, 30, 25, 5, 40, 35])
    heap = HeapClass([25, 35, 30, 15, 10, 25, 5])
    # print(heap.heap)
    # print(heap.heapVerify(0, 1))
    heap.topKFrequent([2, 2, 3, 1, 1, 1])
