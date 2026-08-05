class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        currCombination = []
        length = len(candidates)
        candidates.sort()

        def findCombination(index: int, currSum: int):
            if currSum == target:
                res.append(currCombination.copy())
                return

            for i in range(index, length):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if currSum > target:
                    break
                currCombination.append(candidates[i])
                findCombination(i + 1, currSum + candidates[i])
                currCombination.pop()

        findCombination(0, 0)

        return res