




# Level order traversal

def bredthFirstTraversal(graph, visted, s):
    
    queue=[s]
    visted.add(s)
    while queue:
        curr = queue.pop(0)
        print(curr, end=" ")
        
        for w in graph[curr]:
            if w not in visted:
                visted.add(w)
                queue.append(w)






visted = set()

# Adjacency list
graph = {
    'A': ['B','C','D'],
    'B': ['E'],
    'C': ['E', 'F'],
    'D': ['F'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


bredthFirstTraversal(graph, visted, 'A')