class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])

        visit = [[False for _ in range(m)] for _ in range(n)]

        def checkSizeIsland(i, j: int) -> int:
            if i < 0 or j < 0 or i == n or j == m or grid[i][j] == 0 or visit[i][j]:
                return 0
            size = 1
            visit[i][j] = True
            size += checkSizeIsland(i + 1, j)
            size += checkSizeIsland(i - 1, j)
            size += checkSizeIsland(i, j + 1)
            size += checkSizeIsland(i, j - 1)

            return size


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visit[i][j]:
                    thisSize = checkSizeIsland(i, j)
                    res = max(res, thisSize)    

        return res