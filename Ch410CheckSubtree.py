# T1 and T2 are two very large binary trees, with T1 much bigger than T2.  Create an algorithm to determine if T2 is a subtree of T1.

# A T2 is a subtree if T1 if there exists a node n of subtree T1 that the subtree of n is identical to T2.  That is, if you cut off the tree at node n, the two trees would be identical.

from Ch42MinTree import produceTree
from Ch48FirstCommonAncestor import printTree
from copy import deepcopy

def getRightMostNode(node, depth):
    while depth != 0:
        node = node.right
        depth -= 1
    return node

def preOrderTraversal(node):
    # if node:
    if node == None:
        return 'None'
    return str(node.data) + preOrderTraversal(node.left) + preOrderTraversal(node.right)

# doesn't take into account if there are multiple nodes of the same value of the root of the subtree in the tree.  could be updated to handle this scenario
def isSubtree(tree, subtree):

    if tree == None and subtree == None:
        return True
    elif (tree == None and subtree) or (tree and subtree == None):
        return False

    if tree.data == subtree.data:
        return isSubtree(tree.left, subtree.left) and isSubtree(tree.right, subtree.right)

    if tree and subtree:
        return isSubtree(tree.left, subtree) or isSubtree(tree.right, subtree)
    
def main():
    t1 = produceTree(list(range(1,56)))
    t2 = getRightMostNode(t1, 2) 
    t2 = deepcopy(t2)
    # t2.right = None # if uncommented, both should return false, otherwise both will return true
    print(preOrderTraversal(t2) in preOrderTraversal(t1))
    print(isSubtree(t1, t2))
    # printTree(t1)
    # printTree(t2)

if __name__ == "__main__":
    main()
