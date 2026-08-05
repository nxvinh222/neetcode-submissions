class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1
        farthest = 0
        
        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        if farthest >= lastIndex:
            return True
        return False