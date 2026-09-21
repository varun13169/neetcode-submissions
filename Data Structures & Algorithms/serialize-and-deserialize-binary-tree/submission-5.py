# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        prOr = []
        self.preOrder(root, prOr)

        prS = ""
        for i in prOr:
            prS = prS + "," + str(i)
        prS = prS[1:]

        return prS


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        prOr = data.split(",")
        if prOr[0] == "" or prOr[0] == "None":
            return None
        
        for i in range(len(prOr)):
            if prOr[i] == 'None':
                prOr[i] = None
            else:
                prOr[i] = int(prOr[i])
        
        root = self.createBTP(prOr)
        
        return root


    def preOrder(self, root, res):
        q = [root]

        while len(q) != 0:
            ele = q.pop(0)
            
            if ele != None:
                res.append(ele.val)
                q.append(ele.left)
                q.append(ele.right)
            else:
                res.append(None)


    def createBTP(self, prOr):
        lenPr = len(prOr)
        root = TreeNode(prOr[0])
        q = [root]
        i = 1
        while len(q) != 0:
            r = q.pop(0)
            t = None
            if prOr[i] != None:
                t = TreeNode( prOr[i] )
                q.append(t)
            r.left = t
            i = i + 1


            t = None
            if prOr[i] != None:
                t = TreeNode( prOr[i] )
                q.append(t)
            r.right = t
            i = i + 1        
        return root







