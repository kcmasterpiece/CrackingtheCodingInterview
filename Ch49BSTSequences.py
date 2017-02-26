# A binary search tree was created by traversing through an array from left to right and inserting each element.  Given a binary search tree with distinct elements, print all possible arrays that could have led to the tree.

from Ch42MinTree import produceTree
from Ch48FirstCommonAncestor import printTree
from Chapter3Stacks import Queue
from pprint import pprint

def permutations(node):
    if node.left == None and node.right == None:
        return []
    leftToRight = []
    rightToLeft = []
    if node.left:
        leftToRight.append(node.left.data)
        rightToLeft.append(node.left.data)
    if node.right:
        leftToRight.append(node.right.data)
        rightToLeft.insert(0, node.right.data)
    return [leftToRight, rightToLeft]

# this doesn't quite get us there, but it is close
# this fails because it preserves the order of nodes.  so long as the root of the node comes before any of its descendants, the permutation is considered valid
def sequences(node):
    
    if node == None:
        return []
    perms = permutations(node)
    seqLeft = sequences(node.left)
    seqRight = sequences(node.right)
    seqs = []
    # print('node: {n}, perms: {p}'.format(n=node.data, p=perms))
    if len(seqLeft) == 0 and len(seqRight) == 0:
        for p in perms:
            seqs.append([node.data] + p)
        return seqs
    else:
        for seq in seqLeft:
            for seqR in seqRight:
                    seqs.append([node.data] + seq + seqR)
                    seqs.append([node.data] + seqR + seq)
        return seqs
        
def main():
    tree = produceTree(list(range(1,8)))
    printTree(tree)
    # print(permutations(tree))
    pprint(sequences(tree))

if __name__ == "__main__":
    main()
