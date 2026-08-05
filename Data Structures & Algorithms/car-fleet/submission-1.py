class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        road = [(p, s) for p, s in zip(position, speed)]
        road.sort(reverse=True)

        times = [(target - p)/s for p, s in road]

        prevTime = 0
        for time in times:
            if time > prevTime:
                res += 1
                prevTime = time

        return res
        