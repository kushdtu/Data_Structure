from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNumber(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def median(self):
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0] / 2 + self.min_heap[0] /2
        else:
            return -float(self.max_heap[0])
