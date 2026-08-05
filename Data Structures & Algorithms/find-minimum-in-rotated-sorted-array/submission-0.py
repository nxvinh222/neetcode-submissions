class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if i != len(nums) - 1:
                if nums[i] > nums[i + 1]:
                    return nums[i + 1]
        return nums[0]
        