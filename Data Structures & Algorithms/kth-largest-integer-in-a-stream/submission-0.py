class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create minheap
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        # shorten minheap to K largest integers
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return min(self.minHeap)