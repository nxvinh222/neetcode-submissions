class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last = {}

        for i, char in enumerate(s):
            last[char] = i

        curr = 0
        lastPossiblePosition = 0

        for i, char in enumerate(s):
            curr += 1
            lastPossiblePosition = max(lastPossiblePosition, last[char])
            if i == lastPossiblePosition:
                res.append(curr)
                curr = 0

        return res
