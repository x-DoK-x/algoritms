import random

def barabasi_albert(n=1000, m0=3, m=2):
    # 1. Стартуем с полной сети из m0 узлов
    graph = {i: set(range(m0)) - {i} for i in range(m0)}
    degrees = [m0 - 1] * m0  # Степени начальных вершин

    # 2. Поочередно добавляем N новых узлов
    for new_node in range(m0, m0 + n):
        graph[new_node] = set()
        targets = set()
        
        # Выбираем m уникальных существующих узлов с вероятностью, пропорциональной их степени
        while len(targets) < m:
            # Формируем пул на основе текущих степеней (чем больше степень, тем чаще узел в пуле)
            pool = []
            for node, deg in enumerate(degrees):
                pool.extend([node] * deg)  # Узел повторяется в пуле deg раз
            
            chosen = random.choice(pool)
            if chosen != new_node:
                targets.add(chosen)
        
        # Связываем новый узел с выбранными
        for target in targets:
            graph[new_node].add(target)
            graph[target].add(new_node)
        
        # Обновляем степени (новый узел имеет степень m, у целевых +1)
        degrees.append(m)
        for target in targets:
            degrees[target] += 1

    # 3. Считаем и выводим топ-5 хабов
    final_degrees = [(node, len(neighbors)) for node, neighbors in graph.items()]
    final_degrees.sort(key=lambda x: x[1], reverse=True)
    
    print("Топ-5 узлов-концентраторов (хабов):")
    for i in range(5):
        print(f"Узел {final_degrees[i][0]} - степень {final_degrees[i][1]}")

# Запуск симулятора
barabasi_albert(n=1000, m0=3, m=2)
