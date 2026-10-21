from collections import deque

# Ориентированный граф из задания 3
graph_3 = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['E', 'F'],
    'D': ['G'], 'E': ['G', 'H'], 'F': ['G'], 'G': ['H'], 'H': []
}

# 1. Топологическая сортировка (DFS)
def topological_sort(graph):
    visited = set()
    result = []
    
    def dfs(v):
        visited.add(v)
        for nb in graph.get(v, []):
            if nb not in visited:
                dfs(nb)
        result.append(v)
    
    for v in graph:
        if v not in visited:
            dfs(v)
    return result[::-1]

# 2. Кратчайший путь (BFS)
def shortest_path_bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        vertex, path = queue.popleft()
        if vertex == end:
            return path
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

print("Топологическая сортировка:", topological_sort(graph_3))

path = shortest_path_bfs(graph_3, 'A', 'H')
print(f"Кратчайший путь A -> H: {path}")
if path:
    print(f"Длина пути (число ребер): {len(path) - 1}")
