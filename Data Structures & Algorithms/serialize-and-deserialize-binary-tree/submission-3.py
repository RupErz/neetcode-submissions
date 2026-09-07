# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Encode problem
        final = ""
        def dfs(cur):
            nonlocal final

            if not cur:
                final += "N,"
                return

            # P L R
            final = final + str(cur.val) + ","
            dfs(cur.left)
            dfs(cur.right)
        
        dfs(root)
        return final

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # [1, 2, N, N, 3, 4, N, N, 5, N, N]
        # 1,2,N,N,3,4,N,N,5,N,N
        preorder = data.split(",")
        print(preorder)
        preIdx = 0

        def dfs(data):
            nonlocal preIdx 
            if preIdx >= len(preorder):
                return 

            if preorder[preIdx] == "N":
                preIdx += 1
                return None

            rootVal = int(preorder[preIdx])
            root = TreeNode(rootVal)
            preIdx += 1

            root.left = dfs(data)
            root.right = dfs(data)

            return root
        
        return dfs(data)
