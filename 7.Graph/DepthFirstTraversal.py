def depth_first_travelsal(graph, visted, start):
    if start not in visted:
        print(start, end=" ")
        visted.add(start)
        for w in graph[start]:
            depth_first_travelsal(graph, visted, w)


visted = set()

graph = {
    5: [3,7],
    3: [2,4],
    2: [],
    4: [8],
    8: [],
    7: [8]
}

depth_first_travelsal(graph, visted, 5)