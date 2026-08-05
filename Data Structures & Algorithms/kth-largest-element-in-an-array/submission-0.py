class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negativeNums = [0 - num for num in nums]

        heapq.heapify(negativeNums)

        while k > 0:
            num = heapq.heappop(negativeNums)
            k -= 1

        return 0 - num
        