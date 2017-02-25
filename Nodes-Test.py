from Nodes import *
from igraph import *
import copy
from Chapter3Stacks import Queue

def createGraphNodesFromGraph(graph):
    myGraph = {}
    for v in g.vs:
        v['label'] = v.index
        if v.index not in myGraph:
            myGraph[v.index] = GraphNode(v.index)
        for n in v.neighbors():
            if n.index not in myGraph:
                myGraph[n.index] = GraphNode(n.index)
            myGraph[v.index].nodes.add(myGraph[n.index])
    return myGraph

def colorPlotBidirectionalSearch(graph, path, startVisited,endVisited, vertexStart, vertexEnd):
    for vertex in startVisited:
        v = graph.vs.find(vertex)
        print(startVisited)
        v['color'] = 'blue'

    for vertex in endVisited:
        print(endVisited)
        v = graph.vs.find(vertex)
        v['color'] = 'green'
    for i in range(len(path)):
        if i == 0:
            continue
        # print(path[i-1],path[i])
        edge = graph.es.find(_between=((path[i-1],), (path[i],)))
        edge['color'] = 'purple'

    vertexStart['color'] = 'purple'
    vertexEnd['color'] = 'purple'
    return

def breadthFirstSearchiGraph(graph, start, end):
    q = Queue()
    bfsVertexStart = graph.vs.find(start)
    bfsVertexEnd = graph.vs.find(end)
    parents = { bfsVertexStart.index : None }
    q.add(GraphNode(bfsVertexStart))
    while q.isEmpty() == False:
        vertex = q.remove().data
        vertex['color'] = 'green'
        vertex['label'] = vertex.index
        if vertex == bfsVertexEnd:
            parent = parents[vertex.index] 
            while parent != None:
                parent['color'] = 'blue'
                parent = parents[parent.index] 

            bfsVertexStart['color'] = 'purple'
            bfsVertexStart['label'] = bfsVertexStart.index
            bfsVertexEnd['label'] = bfsVertexEnd.index
            bfsVertexEnd['color'] = 'purple'
            layout = graph.layout_fruchterman_reingold()
            plot(graph, layout=layout)
            break
        for v in vertex.neighbors():
            if v['color'] != 'green':
                parents[v.index] = vertex
                # print(dir(v))
                q.add(GraphNode(v))
    return
g = Graph.Erdos_Renyi(n=75, m=75, directed=True)
# g_bfs = copy.deepcopy(g)
# myGraph = createGraphNodesFromGraph(g) 
# graphKeys = list(myGraph)
# start = random.choice(graphKeys)
# graphKeys.remove(start)
# end = random.choice(graphKeys)
# vertexStart = g.vs.find(start)
# vertexEnd = g.vs.find(end)
# path, startVisited, endVisited = bidirectionalSearch(myGraph[start], myGraph[end])
# colorPlotBidirectionalSearch(g, path, startVisited,endVisited, vertexStart, vertexEnd)

# label vertices
for v in g.vs:
    v['label'] = v.index
# create arrows
for e in g.es:
    e['arrow_width'] = 0.75
    e['arrow_size'] = 0.75
layout = g.layout_fruchterman_reingold(area=1500000)
plot(g, layout=layout)


