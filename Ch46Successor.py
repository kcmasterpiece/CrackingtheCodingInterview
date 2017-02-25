# Successor: Write an algorithm to find the "next" node (i.e. in-order successor) of a given node in a binary search tree.  You may assume that each node has a link to its parent.

from Ch42MinTree import produceTree, TreeNode, traverse
from binarytree import setup, pprint, Node
def createParents(root):
    if getattr(root, 'parent', None) == None:
        root.parent = None

    if root.left:
        root.left.parent = root
        createParents(root.left)

    if root.right:
        root.right.parent = root
        createParents(root.right)


def findParent(node, parent):
    if parent == None:
        print('reached end no parent')
        return None
    if parent.data > node.data:
        print('parent greater than node, returning parent:', parent.data)
        return parent
    print("continuing search for a parent")
    return findParent(node, parent.parent)
        
        

def findSuccessor(node, successor=None):

    print('looking for successor to:', node.data, '\n', 'current successor: ', getattr(successor, 'data', None))
    if successor == None:
        if node.right != None:
            print('successor set to below right')
            successor = node.right
        else:
            print('searching for parent')
            return findParent(node, node.parent)

    if successor != None and successor.left:
        print('traverse down left')
        return findSuccessor(node, successor.left)
    else:
        print('found successor', successor.data)
        return successor





if __name__ == "__main__":
    root = produceTree(list(range(1,30)))
    
    createParents(root)
    # traverse(root)

    # print(findSuccessor(root.right).data)
    setup(
        node_init_func=lambda v: TreeNode(v),
        node_class=TreeNode,
        null_value=None,
        value_attr='data',
        left_attr='left',
        right_attr='right'
    )
    pprint(root)
    print(findSuccessor(root.left.left.right.left))

