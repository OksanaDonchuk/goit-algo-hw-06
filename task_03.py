import networkx as nx
import matplotlib.pyplot as plt
import heapq # Для пріоритетної черги
from typing import Dict, List, Tuple

def create_weighted_graph() -> nx.DiGraph:
    """
    Створює орієнтований зважений граф для моделювання транспортної мережі.

    Returns:
        nx.DiGraph: Орієнтований граф із вагами ребер.
    """
    DG = nx.DiGraph()

    # Вершини (зупинки)
    places: List[str] = [
        "Дім", "Зупинка автобусу", "ст.м. Харківська", "Зупинка трамваю",
        "ст.м. Позняки", "ст.м. Палац спорту", "ст.м. Площа Героїв",
        "ст.м. Золоті ворота", "ст.м. Театральна", "ст.м. Університет", "Робота"
    ]
    DG.add_nodes_from(places)

    # Ребра (маршрути) з вагами (відстанями)
    edges: List[Tuple[str, str, Dict[str, float]]] = [
        ("Дім", "Зупинка автобусу", {"weight": 240}),
        ("Дім", "Зупинка трамваю", {"weight": 470}),
        ("Зупинка автобусу", "ст.м. Харківська", {"weight": 4000}),
        ("Зупинка трамваю", "ст.м. Позняки", {"weight": 1900}),
        ("ст.м. Харківська", "ст.м. Позняки", {"weight": 1200}),
        ("ст.м. Позняки", "ст.м. Палац спорту", {"weight": 9400}),
        ("ст.м. Палац спорту", "Робота", {"weight": 2300}),
        ("ст.м. Палац спорту", "ст.м. Площа Героїв", {"weight": 200}),
        ("ст.м. Площа Героїв", "Робота", {"weight": 1000}),
        ("ст.м. Палац спорту", "ст.м. Золоті ворота", {"weight": 1000}),
        ("ст.м. Золоті ворота", "ст.м. Театральна", {"weight": 200}),
        ("ст.м. Театральна", "ст.м. Університет", {"weight": 800}),
        ("ст.м. Університет", "Робота", {"weight": 540})
    ]
    DG.add_edges_from(edges)
    
    return DG

def visualize_graph(graph: nx.DiGraph) -> None:
    """
    Візуалізує орієнтований зважений граф із кольоровими ребрами та вагами.

    Args:
        graph (nx.DiGraph): Орієнтований граф.
    """
    plt.figure(figsize=(12, 8))
    pos = nx.shell_layout(graph)

    # Кольори ребер
    edge_colors = []
    for edge in graph.edges():
        if edge in [("Дім", "Зупинка автобусу"), ("Зупинка автобусу", "ст.м. Харківська"), 
                    ("ст.м. Харківська", "ст.м. Позняки"), ("ст.м. Палац спорту", "ст.м. Площа Героїв"), 
                    ("ст.м. Площа Героїв", "Робота")]:
            edge_colors.append('skyblue')
        elif edge in [("Дім", "Зупинка трамваю"), ("Зупинка трамваю", "ст.м. Позняки"), 
                      ("ст.м. Палац спорту", "ст.м. Золоті ворота"), ("ст.м. Золоті ворота", "ст.м. Театральна"), 
                      ("ст.м. Театральна", "ст.м. Університет"), ("ст.м. Університет", "Робота")]:
            edge_colors.append('green')
        else:
            edge_colors.append('violet')

    # Малюємо граф із кольоровими ребрами
    nx.draw(graph, pos, with_labels=True, node_color='yellow', node_size=3000, 
            font_size=10, arrows=True, edge_color=edge_colors)

    # Додаємо ваги ребер
    edge_labels = {(u, v): d["weight"] for u, v, d in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, label_pos=0.5)

    plt.title("Мій шлях на роботу")
    plt.show()

def dijkstra(graph: nx.DiGraph, start: str) -> Dict[str, Tuple[float, List[str]]]:
    """
    Реалізує алгоритм Дейкстри для знаходження найкоротших шляхів у графі.

    Args:
        graph (nx.DiGraph): Орієнтований граф.
        start (str): Початкова вершина.

    Returns:
        Dict[str, Tuple[float, List[str]]]: Словник, де ключ – вершина, а значення – кортеж (мінімальна відстань, маршрут).
    """
    # Ініціалізуємо відстані до всіх вершин як "нескінченність"
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0  # Відстань до стартової вершини = 0

    # Ініціалізуємо маршрути (спочатку кожна вершина має порожній маршрут)
    paths = {node: [] for node in graph.nodes}
    paths[start] = [start]  # Стартова вершина сама собі маршрут

    # Використовуємо пріоритетну чергу для вибору вершини з мінімальною відстанню
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Перебираємо сусідів поточної вершини
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда - оновлюємо
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))

    # Повертаємо результат у вигляді словника {вершина: (мінімальна відстань, шлях)}
    return {node: (distances[node], paths[node]) for node in graph.nodes}

if __name__ == "__main__":
    # Створюємо граф із вагами
    graph = create_weighted_graph()
    
    # Візуалізуємо граф
    visualize_graph(graph)

    # Вибираємо стартову вершину
    start = "Дім"

    # Виконуємо алгоритм Дейкстри
    shortest_paths = dijkstra(graph, start)

    # Виводимо найкоротші шляхи від "Дім" до всіх вершин
    print("\n🔍 Найкоротші шляхи від вершини 'Дім':")
    for node, (distance, path) in shortest_paths.items():
        print(f"🔹 Від 'Дім' до '{node}': шлях = {path}, відстань = {distance}")