class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        visited = []
        for i in range(m):
             t = [0] * n
             visited.append(t)

        pacificSet = set()
        for i in range(n):
            self.dfs(0, i, heights, pacificSet, visited)
        for i in range(m):
            self.dfs(i, 0, heights, pacificSet, visited)


        visited = []
        for i in range(m):
             t = [0] * n
             visited.append(t)
        atlanticSet = set()
        for i in range(n):
            self.dfs(m-1, i, heights, atlanticSet, visited)
        for i in range(m):
            self.dfs(i, n-1, heights, atlanticSet, visited)
        
        # print(pacificSet)
        # print(atlanticSet)

        finalList = []
        for i in pacificSet:
            for j in atlanticSet:
                if i[0] == j[0] and i[1] == j[1]:
                    finalList.append( [i[0], i[1]] )
        
        # print(finalSet)

        return finalList



    def dfs(self, r, c, heights, canReachSet, visited):
        m = len(heights)
        n = len(heights[0])
        canReachSet.add( (r, c) )
        visited[r][c] = 1

        dx = [+1, -1, 0, 0]
        dy = [0, 0, +1, -1]
        dxyLen = len(dx)

        for i in range(dxyLen):
            newR = r + dx[i]
            newC = c + dy[i]
            if newR >= 0 and newR <= m-1 and newC >= 0 and newC <= n-1 and heights[newR][newC] >= heights[r][c]:
                if visited[newR][newC] == 0:
                    self.dfs(newR, newC, heights, canReachSet, visited)

        