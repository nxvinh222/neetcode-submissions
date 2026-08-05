class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSet = []

        def getSubSets(index: int):
            res.append(subSet.copy())
            if len(subSet) == len(nums):
                return

            for i in range(index, len(nums)):
                subSet.append(nums[i])
                getSubSets(i + 1)
                subSet.pop()

        getSubSets(0)
        return res