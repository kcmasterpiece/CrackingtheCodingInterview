# Given a binary tree, design an algorithm which creates a list of all nodes at each depth

from Ch42MinTree import produceTree
from Chapter3Stacks import LinkedList


def traverse(root):
    level = LinkedList()
    level.insert(root)
    levelNode = level.first
    # print(dir(levelNode.data))
    level.printSelf() 
    while levelNode != None:
        newLevel = LinkedList()
        node = levelNode
        while node != None and node.data != None:
            if node.data.left: newLevel.insert(node.data.left)
            if node.data.right: newLevel.insert(node.data.right)
            node = node.next

        newLevel.printSelf()
        levelNode = newLevel.first

if __name__ == "__main__":
    root = produceTree([1,2,3,4,5,6,7,8])
    traverse(root)

