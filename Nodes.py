import random
from igraph import *
from Chapter3Stacks import Queue
class Node:
    def __init__(self, data):
        """initialize node, set node data to value passed

        :data: TODO
        :returns: TODO

        """
        self.data = data
        return

class GraphNode(Node):
    def __init__(self, data):
        """initialize node, set node data to value passed
        set neighbors equal to empty set
        """
        self.data = data
        self.nodes = set() 
        return

def depthFirstSearch(node, visited=None):
    """ performs depth-first search on graph
    visited is an empty set
    """
    if visited == None:
        visited = set()

    if node == None: 
        return
    
    visited.add(node)
    print("Visited: " + node.data)
    for n in (node.nodes - visited):
        depthFirstSearch(n, visited)
    return

def breadthFirstSearch(node):
    """ performs breadth-first search on graph

    """
    q = Queue()
    visited = set()
    q.add(node)
    while q.isEmpty() == False:
        node = q.remove() 
        visited.add(node)
        for n in (node.nodes - visited):
            q.add(n)
        print("visiting:", node.data)
    return
   
def bidirectionalSearch(start, end):
    def getPath(node, visited):
        path = list()
        path.insert(0, node.data)
        for root in ['start','end']:
            parent = getattr(node, root, None)
            # print(parent)
            while parent != None:
                path.insert(0, parent.data)
                parent = getattr(parent, root, None)
            path.reverse()
        return path

    visited = {'start': set(), 'end': set()  }
    q = Queue()
    print('start:', start.data, ' end:', end.data)
    start.home = 'start'
    end.home = 'end'
    q.add(start)
    q.add(end)
    while q.isEmpty() == False:
        node = q.remove()
        visited[node.home].add(node)
        # print("{b} ({c}) has neightbor nodes: {a}".format(a = list(map(lambda x: x.data, node.nodes)), b = node.data, c = node.home))
        # print("start visited: {a}".format(a = list(map(lambda x: x.data, visited['start']))))
        # print("end visited: {a}".format(a = list(map(lambda x: x.data,visited['end']))))
        # print("nodes - visited['{b}']: {a}".format(a = list(map(lambda x: x.data,node.nodes - visited[node.home])), b = node.home))
        for n in node.nodes - visited[node.home]:
            setattr(n, 'home', node.home) 
            setattr(n, node.home, node) 
            if (node.home == 'start' and n in visited['end']) or (node.home == 'end' and n in visited['start']):
                visited[node.home].add(n)
                path = getPath(n, visited)
                return (path, list(map(lambda x: x.data,visited['start'])), list(map(lambda x: x.data,visited['end'])))
            q.add(n)
        # q.printSelf()
        # print('visited:', node.data)
