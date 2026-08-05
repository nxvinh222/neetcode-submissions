class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = l + (r - l) // 2

            cost = self.calculateCost(piles, mid)
            if cost > h:
                l = mid + 1
            else:
                r = mid - 1
                res = mid

        return res

    def calculateCost(self, piles: List[int], speed) -> int:
        res = 0

        for pile in piles:
            res += math.ceil(float(pile)/speed)

        return res
        