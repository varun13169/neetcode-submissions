class Solution:
    def findNode(self, src, adjList, visited, childParentMap, nodeInCycle):
        visited[src] = 1
        adjL = adjList[src]
        for adj in adjL:
            if visited[adj] == 0:
                childParentMap[adj] = src
                self.findNode(adj, adjList, visited, childParentMap, nodeInCycle)
            else: 
                if childParentMap[src] != adj and nodeInCycle[0] == -1:
                    nodeInCycle[0] = adj
                    childParentMap[adj] = src


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        lenE = len(edges)
        adjList = {}

        for i in range(lenE):
            edge = edges[i]
            n1 = edge[0] - 1
            n2 = edge[1] - 1
            n1AdL = adjList.get(n1, [])
            n2AdL = adjList.get(n2, [])
            
            n1AdL.append(n2)
            n2AdL.append(n1)
            adjList[n1] = n1AdL
            adjList[n2] = n2AdL
        
        q = []
        visited = [0] * lenE
        q.append(0)
        visited[0] = 1
        childParentMap = {0: None}
        nodeInCycle = [-1]

        self.findNode(0, adjList, visited, childParentMap, nodeInCycle)
        
        nodeInCycle = nodeInCycle[0]
        parentMap = {}
        st = childParentMap[nodeInCycle]

        while st != nodeInCycle:
            parentMap[st] = 1
            st = childParentMap[st]
            parentMap[st] = 1

        print(parentMap)
        print(childParentMap)
        for i in range(lenE-1, -1, -1):
            edge = edges[i]
            n1 = edge[0] - 1
            n2 = edge[1] - 1
            if parentMap.get(n1, "N") != "N" and parentMap.get(n2, "N") != "N":
                return edge

        return None






        