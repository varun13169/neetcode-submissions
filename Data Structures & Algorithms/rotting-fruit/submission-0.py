class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        hasChanged = True
        m = len(grid)
        n = len(grid[0])
        rotten = 2

        while hasChanged:
            hasChanged = False

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == rotten:
                        # check adjacent and make them rotten+1
                        if j > 0 and grid[i][j-1] == 1:
                            grid[i][j-1] = rotten+1
                            hasChanged = True
                        if j < n-1 and grid[i][j+1] == 1:
                            grid[i][j+1] = rotten+1
                            hasChanged = True

                        if i > 0 and grid[i-1][j] == 1:
                            grid[i-1][j] = rotten+1
                            hasChanged = True
                        if i < m-1 and grid[i+1][j] == 1:
                            grid[i+1][j] = rotten+1
                            hasChanged = True
            
            minute = minute + 1
            rotten = rotten + 1
        
        # check if fresh is left
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return minute - 1


        