import networkx as nx
from typing import List, Optional
from task_01 import create_graph  # Імпортуємо функцію з першого завдання

def dfs(graph: nx.DiGraph, start: str, target: str, path: Optional[List[str]] = None) -> Optional[List[str]]:
    """
    Реалізація алгоритму пошуку в глибину (DFS) для знаходження шляху у графі.

    Args:
        graph (nx.DiGraph): Орієнтований граф.
        start (str): Початкова вершина.
        target (str): Цільова вершина.
        path (Optional[List[str]]): Шлях, що формується рекурсивно.

    Returns:
        Optional[List[str]]: Перший знайдений шлях від `start` до `target`, або None, якщо шлях не знайдено.
    """
    if path is None:
        path = []
    path = path + [start]

    if start == target:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, target, path)
            if new_path:
                return new_path
    return None

def bfs(graph: nx.DiGraph, start: str, target: str) -> Optional[List[str]]:
    """
    Реалізація алгоритму пошуку в ширину (BFS) для знаходження найкоротшого шляху у графі.

    Args:
        graph (nx.DiGraph): Орієнтований граф.
        start (str): Початкова вершина.
        target (str): Цільова вершина.

    Returns:
        Optional[List[str]]: Найкоротший шлях від `start` до `target`, або None, якщо шлях не знайдено.
    """
    queue = [(start, [start])]

    while queue:
        vertex, path = queue.pop(0)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in path:
                if neighbor == target:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    
    graph = create_graph()

    start, target = "Дім", "Робота"

    path_dfs = dfs(graph, start, target)
    path_bfs = bfs(graph, start, target)

    print(f"Шлях з {start} до {target} за допомогою DFS: {path_dfs}")
    print(f"Шлях з {start} до {target} за допомогою BFS: {path_bfs}")
