from collections import deque

# Граф из задания 2
graph_2 = {
    'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D'], 'D': ['C'],
    'E': ['F'], 'F': ['E', 'G'], 'G': ['F'],
    'H': [],
    'I': ['J', 'L'], 'J': ['I', 'K'], 'K': ['J', 'L'], 'L': ['K', 'I']
}

# 1. Поиск компонент связности
def find_components(graph):
    visited = set()
    components = []
    for vertex in graph:
        if vertex not in visited:
            component = set()
            stack = [vertex]
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    component.add(v)
                    for nb in graph[v]:
                        if nb not in visited:
                            stack.append(nb)
            components.append(component)
    return components

# 2. Проверка двудольности через BFS
def is_bipartite(graph, start):
    color = {start: 0}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for nb in graph[v]:
            if nb not in color:
                color[nb] = 1 - color[v]
                queue.append(nb)
            elif color[nb] == color[v]:
                return False, None
    return True, color

print("Компоненты связности:")
comps = find_components(graph_2)
for i, comp in enumerate(comps, 1):
    print(f"Компонента {i}: {comp}")
    
    # Проверяем каждую компоненту на двудольность
    start_node = list(comp)[0]
    ok, coloring = is_bipartite(graph_2, start_node)
    if ok:
        print(f"  Двудольный. Раскраска: {coloring}")
    else:
        print("  Недвудольный (содержит цикл нечетной длины).")
