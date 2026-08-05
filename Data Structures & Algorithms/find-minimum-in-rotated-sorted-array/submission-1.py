class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return nums[0]

        while l <= r:
            mid = l + (r - l)//2
            if (mid == 0 and nums[mid] < nums[mid + 1]) or (mid == len(nums) - 1 and nums[mid] < nums[mid - 1]) or (
                    nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]):
                return nums[mid]
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[mid]
        