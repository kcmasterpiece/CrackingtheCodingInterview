# Implement a function to check if a binary tree is a binary search tree

# Properties of a binary tree:
#   -All descendents of the left node are less than the root node
#   -All descendents of the right node are greater than the root node

from Ch42MinTree import produceTree, TreeNode
# from Ch43ListDepths import traverse

def checkBST(node, nodeMin=None, nodeMax=None):
    if node == None:
        return True

    # print(node.data, nodeMin, nodeMax)
    if (nodeMin == None or node.data >= nodeMin) and (nodeMax == None or node.data < nodeMax):
        return checkBST(node.left, nodeMin, node.data) and checkBST(node.right, node.data, nodeMax)
    else:
        return False

if __name__ == "__main__":
    root = produceTree(list(range(1,9)))
    # traverse(root)
    print(checkBST(root)) # True
    root.left.right.right = TreeNode(10)
    # traverse(root)
    print(checkBST(root)) # False
    root = produceTree(list(range(1,9)))
    root.right = TreeNode(1)
    print(checkBST(root)) # False
