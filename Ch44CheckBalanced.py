# Implement a function to check if a binary tree is balanced.  For the purposes of this question, a balanced tree is defined to be a tree such that the hights of two subtress never differ by more than one.


from Ch42MinTree import produceTree, TreeNode

def getHeight(tree):
    if tree == None:
        return -1
    return max(getHeight(tree.left), getHeight(tree.right)) + 1

def checkBalanced(tree):
    if tree == None:
        return True
    if abs(getHeight(tree.left) - getHeight(tree.right)) > 1:
        return False
    else:
        return checkBalanced(tree.left) and checkBalanced(tree.right)

def checkHeight(tree):
    if tree == None:
        return -1
    
    leftHeight = checkHeight(tree.left)
    if leftHeight == -2: 
        return -2
    rightHeight = checkHeight(tree.right)
    if rightHeight == -2: 
        return -2
    
    if abs(leftHeight - rightHeight) > 1:
        return -2
    else:
        return max(checkHeight(tree.left), checkHeight(tree.right))+1

root = produceTree( list(range(1,9)) )
print(checkHeight(root))
print(checkBalanced(root)) # True
root.right = None
print(checkBalanced(root)) # False
