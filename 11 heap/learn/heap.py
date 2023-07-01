# Max heap
class HeapClass:
    def __init__(self, arr=[]):
        # self.heap = arr
        if arr != []:
            self.size = 1
            self.heap = [arr[0]]
            for i in range(1,len(arr)):
                self.insert(arr[i])
        # self.buildHeap()    

    # def buildHeap(self):
    #     for i in range(self.size//2-1, -1, -1):
    #         self.percolateDown(i)
            
    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        k = self.size -1

        while k!=0 and self.heap[k] > self.heap[k//2]:
            self.heap[k],self.heap[k//2] = self.heap[k//2],self.heap[k]
            k = k//2

    def delete(self):
        if self.size == 0:
            return -1
        self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
        self.size -= 1
        

    
    
        # self.heap[k] = x
        # self.percolateUp(self.size-1)

    # def percolateUp(self, i):
    #     while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
    #         self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
    #         i = self.parent(i)

    # def parent(self, i):
    #     return (i)//2
    
    

if __name__ == "__main__":
    heap = HeapClass([10, 20, 30,25,5,40,35])
    print(heap.heap)