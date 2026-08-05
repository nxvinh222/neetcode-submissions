class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def calculate(position: int) -> int:
            if position == 0:
                return 1
            if position < 0:
                return 0

            if position in memo:
                return memo[position]

            res = calculate(position - 1) + calculate(position - 2)

            memo[position] = res

            return res

        return calculate(n)
        