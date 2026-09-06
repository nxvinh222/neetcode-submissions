class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        start = 0
        end = k - 1

        sumThreshold = k * threshold

        s = 0
        for i in range(0, k):
            s += arr[i]

        while True:
            if s >= sumThreshold:
                res += 1
            s -= arr[start]
            start += 1
            end += 1
            if end == len(arr):
                break
            s += arr[end]

        return res