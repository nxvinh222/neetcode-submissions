class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        count = 0
        lastIndex = len(nums) - 1
        currIndex = 0

        while farthest < lastIndex:
            localFarthest = farthest
            for i in range(currIndex, farthest + 1):
                if i + nums[i] > localFarthest:
                    localFarthest = i + nums[i]
                    currIndex = i
            count += 1
            farthest = localFarthest

        return count

        
        