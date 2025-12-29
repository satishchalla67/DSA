







def breadthfirsttraversal(graph, visted, s):
    queue = [s]
    while queue:
        curr = queue.pop(0)
        if curr not in visted:
            print(curr, end=" ")
            visted.add(curr)
            for w in graph[curr]:
                queue.append(w)
            





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

breadthfirsttraversal(graph, visted, 'A')