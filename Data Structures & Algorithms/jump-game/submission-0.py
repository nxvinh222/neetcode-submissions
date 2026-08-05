class Solution:
    def canJump(self, nums: List[int]) -> bool:
        power = nums[0]
        currPosition = 0
        lastIndex = len(nums) - 1
        if lastIndex == 0:
            return True

        while power > 0:
            maxNextPower = 0
            maxNextPowerIndex = currPosition
            
            for i in range(currPosition + 1, currPosition + power + 1):
                if i > lastIndex:
                    break
                if i - currPosition + nums[i] > maxNextPower:
                    maxNextPower = i - currPosition + nums[i]
                    maxNextPowerIndex = i

            currPosition = maxNextPowerIndex
            power = nums[currPosition]
            if currPosition + power >= lastIndex:
                return True

        return False
        