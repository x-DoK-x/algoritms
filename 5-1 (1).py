from collections import deque

# Граф из задания 1
graph_1 = {
    '1': ['2', '3'], '2': ['1', '4', '5'], '3': ['1', '6', '7'],
    '4': ['2', '8'], '5': ['2', '8'], '6': ['3', '9'], '7': ['3', '9'],
    '8': ['4', '5', '10'], '9': ['6', '7', '10'], '10': ['8', '9']
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

print("DFS от 1:", end=' ')
dfs(graph_1, '1')
print("\nBFS от 1:", bfs(graph_1, '1'))
