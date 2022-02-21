# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.rob_dict = {}

    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return root.val
        elif root in self.rob_dict:
            return self.rob_dict[root]

        l_val = 0
        r_val = 0
        ll_val = 0
        lr_val = 0
        rl_val = 0
        rl_val = 0
        rr_val = 0
        if root.left is not None:
            if root.left.left is not None:
                ll_val = self.rob(root.left.left)
            if root.left.right is not None:
                lr_val = self.rob(root.left.right)
            l_val = self.rob(root.left)

        if root.right is not None:
            if root.right.left is not None:
                rl_val = self.rob(root.right.left)
            if root.right.right is not None:
                rr_val = self.rob(root.right.right)
            r_val = self.rob(root.right)

        self.rob_dict[root] = max(root.val+ll_val+lr_val+rl_val+rr_val, l_val+r_val)
        # print("{} {} {}".format(len(self.rob_dict), root.val, id(root)))
        return self.rob_dict[root]
