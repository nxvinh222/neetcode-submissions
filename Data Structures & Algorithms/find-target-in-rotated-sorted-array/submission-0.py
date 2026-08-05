class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l)//2

            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        if target > nums[-1]:
            l = 0
            r = pivot - 1
        elif target < nums[-1]:
            l = pivot
            r = len(nums) - 1
        else:
            return len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
        