# Max heap
class HeapClass:
    def __init__(self, arr=[]):
        self.heapiFy(arr)
        # if arr != []:
        #     self.size = 1
        #     self.heap = [arr[0]]
        #     for i in range(1, len(arr)):
        #         self.insert(arr[i])

    # def buildHeap(self):
    #     for i in range(self.size//2-1, -1, -1):
    #         self.percolateDown(i)

    def heapiFy(self, arr):
        self.heap = arr
        self.size = len(arr)

        # for i in range(self.size//2-1, -1, -1):
        #     j = 2*i + 1
        #     while j <= self.size - 1:
        #         if j < self.size - 1 and self.heap[j] < self.heap[j + 1]:
        #             j += 1
        #         if self.heap[i] < self.heap[j]:
        #             self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        #             i = j
        #             j = j * 2
        #         else:
        #             break

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

    def heapVerify(self, i, j):
        if self.size == 0:
            return False

        if j >= self.size-1:
            return True
        else:
            if self.heap[i] < self.heap[j]:
                return False
            val = self.heapVerify(j, j*2)
            val = self.heapVerify(j, j*2+1)
        return val
        # while j <= self.size - 1:
        #     if self.heap[i] > self.heap[j]:
        #         i = j
        #         j = j * 2
        #     else:
        #         break
        # while j <= self.size - 1:
        #     if self.heap[i] < self.heap[j]:
        #         # self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        #         i = j
        #         j = j * 2 + 1
        #     else:
        #         break


if __name__ == "__main__":
    # heap = HeapClass([10, 20, 30, 25, 5, 40, 35])
    heap = HeapClass([25, 35, 30, 15, 10, 25, 5])
    print(heap.heap)
    print(heap.heapVerify(0, 1))
    # # heap.insert(80)
    # # print(heap.heap)
    # heap.delete()
    # print(heap.heap)
    # heap.delete()
    # print(heap.heap)
    # heap.delete()
    # print(heap.heap)
    # heap.delete()
    # print(heap.heap)
    # heap.delete()
    # print(heap.heap)
    # heap.delete()
    # print(heap.heap)
