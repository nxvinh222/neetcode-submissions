class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        total = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            total += gas[i]
            total -= cost[i]
            if total < 0:
                total = 0
                res = i + 1

        if res < len(gas):
            return res
        return -1


        