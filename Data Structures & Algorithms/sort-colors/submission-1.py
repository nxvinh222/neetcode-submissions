class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = -1
        r = len(nums)
        i = 0
        while i < r:
            if nums[i] == 0:
                l += 1
                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp
                i += 1
            elif nums[i] == 2:
                r -= 1
                temp = nums[r]
                nums[r] = nums[i]
                nums[i] = temp
            else:
                i += 1


            

        