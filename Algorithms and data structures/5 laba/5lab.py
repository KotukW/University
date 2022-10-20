def findLowestCostNode(nodeCosts):
    lowestCost = float("inf")
    lowestCostNode = None
    for node in nodeCosts:
        cost = nodeCosts[node]
        if cost < lowestCost and node not in processed:
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode

def findWay(graph, startNode, EndNode):
    global processed
    nodeCosts = dict(graph[startNode])
    infinity = float("inf")
    
    for key in graph:
        if key not in nodeCosts:
            nodeCosts[key] = infinity
    parents = {}
    
    for value in graph[startNode]: 
        parents[value] = startNode    
    
    processed = []
    node = findLowestCostNode(nodeCosts) 
    while node is not None:  
        cost = nodeCosts[node]
        neighbors = graph[node]
        for n in neighbors.keys(): 
            newCost = cost + neighbors[n] 
            if nodeCosts[n] > newCost: 
                nodeCosts[n] = newCost 
                parents[n] = node 
        processed.append(node) 
        node = findLowestCostNode(nodeCosts) 
    return nodeCosts[EndNode]

graph = {}
firstNode, secondNode = int(input()), int(input())
with open('5 laba\\graph.txt', 'r') as fr:
    for string in fr:
        stringWOn = string.strip("\n")
        splittedString = stringWOn.split(":")
        graphNode = int(splittedString[0])
        graph[graphNode] = {}
        graphConnectedNodes = splittedString[1].split()
        for nodeAndWeight in graphConnectedNodes:
            splitted = nodeAndWeight.split("-")
            graph[graphNode][int(splitted[0])] = int(splitted[1])
print(findWay(graph, firstNode, secondNode))
