class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])

        mem = [0] * len(nums)
        mem[0] = nums[0]
        mem[1] = max(nums[0], nums[1])
        mem[2] = max(nums[1], nums[0] + nums[2])

        for i in range(3, len(nums)):
            mem[i] = max(mem[i - 2], mem[i - 3]) + nums[i]

        return max(mem[-1], mem[-2])
        