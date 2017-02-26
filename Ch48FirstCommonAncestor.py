# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure.  NOTE: This is not necessarily a binary search tree.

from Chapter3Stacks import LinkedList
from Ch42MinTree import produceTree, TreeNode
from Ch46Successor import createParents
from binarytree import setup, pprint, Node

def checkListforNode(node, linkedList):
    current = linkedList.first
    while current:
        if node.data == current.data:
            return node
        current = current.next
    return None

# this approach takes way too long-- o(log n)?  a better solution would find the depths of both nodes, and once they are on even footing, traverse to the parent
def firstCommonAncestorBad(nodeA, nodeB):
    pathA = LinkedList()
    pathB = LinkedList()
    while nodeA or nodeB:

        if nodeA:
            pathA.insert(nodeA.data)
            if checkListforNode(nodeA, pathB) != None:
                return nodeA
            nodeA = nodeA.parent
        if nodeB:
            pathB.insert(nodeB.data)
            if checkListforNode(nodeB, pathA) != None:
                return nodeB
            nodeB = nodeB.parent

    return None
        
def depth(node):
    depth = 0
    while node.parent:
        node = node.parent
        depth += 1
    return depth

def adjust(node, depth):
    while depth > 0:
        node = node.parent
        depth -= 1
    return node

def firstCommonAncestor(nodeA, nodeB):
    print('nodeA: {a}  nodeB: {b}'.format(a=nodeA.data, b=nodeB.data))
    difference = depth(nodeA) - depth(nodeB)
    
    if difference < 0:
        nodeB = adjust(nodeB, abs(difference))
    else:
        nodeA = adjust(nodeA, difference)
    
    while nodeA != nodeB:
        
        nodeA = getattr(nodeA, 'parent', None)    
        nodeB = getattr(nodeB, 'parent', None)
        
    if nodeA == None or nodeB == None: 
        return None
    else:
        return nodeA
    
    

def printTree(tree):
    setup(
        node_init_func=lambda v: TreeNode(v),
        node_class=TreeNode,
        null_value=None,
        value_attr='data',
        left_attr='left',
        right_attr='right'
    )
    pprint(tree)
    return

def main():
    tree = produceTree(list(range(1,25)))
    printTree(tree)
    createParents(tree)
    print(firstCommonAncestor(tree.right.right, tree.right.left.left.left).data)

if __name__ == "__main__":
    main()
