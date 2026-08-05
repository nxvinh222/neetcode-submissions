class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        res = 0

        def dfs(i, j: int):
            if i not in range(len(grid)) or j not in range(len(grid[0])) or visit[i][j] or grid[i][j] == "0":
                return
            visit[i][j] = True
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if visit[i][j] or grid[i][j] == "0":
                    continue
                dfs(i, j)
                res += 1

        return res
        