# Max heap
class HeapClass:
    def __init__(self, arr=[]):
        self.heapiFy(arr)

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
        return self.heap[self.size]


if __name__ == "__main__":
    # heap = HeapClass([10, 20, 30, 25, 5, 40, 35])
    heap = HeapClass([3, 2, 1, 5, 6, 4])
    print(heap.heap)

    for i in range(2):
        print(heap.delete())
    # print(heap.heap)
