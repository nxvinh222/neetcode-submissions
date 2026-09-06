class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        res = 100001
        currSum = nums[0]

        while True:
            while currSum - nums[start] >= target:
                currSum -= nums[start]
                start += 1

            if currSum >= target:
                res = min(res, end - start + 1)
            
            end += 1
            if end == len(nums):
                break

            currSum += nums[end]

        if res == 100001:
            return 0
        return res