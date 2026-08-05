class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def rob1(numsList: List[int]) -> int:
            mem = [0] * len(numsList)
            mem[0] = numsList[0]
            mem[1] = max(numsList[0], numsList[1])
            for i in range(2, len(numsList)):
                mem[i] = max(mem[i - 1], mem[i - 2] + numsList[i])

            return mem[-1]

        return max(rob1(nums[:-1]), rob1(nums[1:]))