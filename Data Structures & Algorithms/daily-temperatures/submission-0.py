class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        mem = []

        for i, v in enumerate(temperatures):
            while len(mem) > 0 and v > mem[-1][0]:
                print(0)
                _, index = mem.pop()
                res[index] = i - index

            mem.append([v, i])

        return res
        