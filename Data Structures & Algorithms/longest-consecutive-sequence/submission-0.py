class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mem = set(nums)

        res = 0

        for num in mem:
            if num - 1 not in mem:
                consecutive = 0
                numInSequence = num
                while numInSequence in mem:
                    consecutive += 1
                    numInSequence += 1
                res = max(res, consecutive)

        return res
        