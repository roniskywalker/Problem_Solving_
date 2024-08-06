class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(x,y,l,memo):
            if x<0 or x>=m or y<0 or y>=n or l[x][y]==1 or l[x][y]==2:
                return 0
            if x==m-1 and y==n-1:
                return 1
            if (x,y) in memo:
                return memo[(x,y)]
            memo[(x,y)] = 0
            l[x][y] = 2
            memo[(x,y)] += dfs(x+1,y,l,memo)
            memo[(x,y)] += dfs(x,y+1,l,memo)
            l[x][y] = 0
            return memo[(x,y)]
        return dfs(0,0,grid,{})