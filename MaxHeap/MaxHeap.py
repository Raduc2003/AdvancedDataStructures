class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return int((i-1)/2)

    def leftChild(self, i):
        return int((2*i)+1)

    def rightChild(self, i):
        return int((2*i)+2)

    def insert(self, key):
        i = len(self.heap)
        self.heap.append(key)
        if key > self.heap[i-1]:
            while self.heap[i] > self.heap[int((i-1)/2)]:
                self.heap[int(
                    (i-1)/2)], self.heap[i] = self.heap[i], self.heap[int((i-1)/2)]
                i = int((i-1)/2)

    def printHeap(self):
        print(self.heap)

    def deleteAt(self, i):
        self.heap[i], self.heap[len(
            self.heap)-1] = self.heap[len(self.heap)-1], self.heap[i]
        self.heap.pop(len(self.heap)-1)
        self.heapDown(i)

    def heapDown(self, i):
        max = i
        left = self.leftChild(i)
        right = self.rightChild(i)
        if left < len(self.heap) and self.heap[left] > self.heap[max]:
            max = left
        if right < len(self.heap) and self.heap[right] > self.heap[max]:
            max = right
        if i != max:
            self.heap[max], self.heap[i] = self.heap[i], self.heap[max]
            self.heapDown(max)

    def extractRoot(self):
        self.deleteAt(0)

    def join(self, heap):
        self.heap.extend(heap.heap)
        heap.heap.clear()
        heapify(self)


def heapify(heap):
    i = int(len(heap.heap)/2-1)
    while (i >= 0):
        heap.heapDown(i)
        i -= 1


# h1 = MaxHeap()
# h2 = MaxHeap()
# h1.insert(12)
# h1.insert(9)
# h1.insert(10)
# h2.insert(2)
# h2.insert(3)
# h2.insert(1)
# h1.join(h2)

# h1.printHeap()
# h2.printHeap()
