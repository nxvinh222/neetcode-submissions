class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            res = []
            mem = set()
            k = 0

            nums.sort()

            for i, v in enumerate(nums):
                if v >= 0:
                    mem.add(v)

            for i, v in enumerate(nums):
                if i > 0 and v == nums[i - 1]:
                    continue
                if v > 0:
                    break
                sum = v
                for j in range(i + 1, len(nums) - 1):
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        continue
                    sum = v + nums[j]
                    if sum <= 0:
                        remain = k - sum
                        if remain == nums[j]:
                            if nums[j] == nums[j + 1]:
                                res.append([v, nums[j], nums[j + 1]])
                        else:
                            if remain in mem and remain > nums[j]:
                                res.append([v, nums[j], remain])
                    else:
                        break

            return res
        