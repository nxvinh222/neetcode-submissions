class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []

        def getSubSet(index: int, sum: int):
            if sum == target:
                res.append(subSet.copy())
            if sum > target:
                return

            for i in range(index, len(candidates)):
                subSet.append(candidates[i])
                getSubSet(i, sum + candidates[i])
                subSet.pop()

        getSubSet(0, 0)

        return res
        