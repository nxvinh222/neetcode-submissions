class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            minHeap.append((point[0] * point[0] + point[1] * point[1], point[0], point[1]))

        heapq.heapify(minHeap)
        
        res = []
        while len(res) < k:
            node = heapq.heappop(minHeap)
            res.append([node[1], node[2]])
        return res
        