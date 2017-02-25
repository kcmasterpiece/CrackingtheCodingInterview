from Chapter3Stacks import Node, Queue

class TreeNode(Node):
    def __init__(self, x=None, left=None, right=None):
       self.data = x
       self.left = left
       self.right = right

def produceTree(data=[1,2,3,4,5,6,7,8]):
    root = None
    if len(data) == 0:
        return None

    left = produceTree(data[0:int(len(data)/2)])
    right = produceTree(data[int(len(data)/2)+1:])
    root = TreeNode(x=data[int(len(data)/2)], left=left, right=right)
    
    return root

def traverse(root):
    level = 0
    thislevel = [root]

    while thislevel:
        nextlevel = list()
        level += 1
        print('level: ',level)
        for n in thislevel:
            print(n.data)
            if n.left: nextlevel.append(n.left)
            if n.right: nextlevel.append(n.right)
        print()
        thislevel = nextlevel

if __name__ == '__main__':
    data = list(range(1,9))
    tree = produceTree(data=data)
    traverse(tree)



    

