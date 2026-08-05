class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        mem = set()

        def buildString():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in mem:
                    curr.append(nums[i])
                    mem.add(nums[i])
                    buildString()
                    curr.pop()
                    mem.remove(nums[i])

        buildString()

        return res