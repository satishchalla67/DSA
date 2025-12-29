







def depthfirsttraversal(graph, visted, s):
    if s not in visted:
        visted.add(s)
        print(s)
        for w in graph[s]:
            depthfirsttraversal(graph, visted, w)






visted=set()


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['E', 'F'],
    'D': ['F'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

depthfirsttraversal(graph, visted, 'A')