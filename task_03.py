import networkx as nx
import matplotlib.pyplot as plt
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

def find_shortest_paths(graph: nx.DiGraph) -> Dict[str, Dict[str, Tuple[List[str], float]]]:
    """
    Використовує алгоритм Дейкстри для знаходження найкоротших шляхів між усіма вершинами.

    Args:
        graph (nx.DiGraph): Орієнтований зважений граф.

    Returns:
        Dict[str, Dict[str, Tuple[List[str], float]]]: Словник найкоротших шляхів та їхньої довжини між усіма вершинами.
    """
    shortest_paths: Dict[str, Dict[str, Tuple[List[str], float]]] = {}

    for source in graph.nodes:
        shortest_paths[source] = {}
        for target in graph.nodes:
            if source != target:
                try:
                    path = nx.dijkstra_path(graph, source=source, target=target)
                    distance = nx.dijkstra_path_length(graph, source=source, target=target)
                    shortest_paths[source][target] = (path, distance)
                except nx.NetworkXNoPath:
                    shortest_paths[source][target] = ([], float('inf'))  # Якщо шлях не існує
    
    return shortest_paths

if __name__ == "__main__":
    # Створюємо граф із вагами
    graph = create_weighted_graph()
    
    # Візуалізуємо граф
    visualize_graph(graph)

    # Знаходимо найкоротші маршрути від усіх вершин
    shortest_paths = find_shortest_paths(graph)

    # Виводимо найкоротший шлях від "Дім" до "Робота"
    start, target = "Дім", "Робота"
    if target in shortest_paths[start]:
        path, distance = shortest_paths[start][target]
        print(f"\nНайкоротший шлях від '{start}' до '{target}': {path}")
        print(f"Відстань: {distance}")
    else:
        print(f"Шляху від '{start}' до '{target}' не існує.")

    # Вивід усіх найкоротших шляхів
    print("\nНайкоротші шляхи між усіма вершинами:")
    for src, targets in shortest_paths.items():
        for dest, (path, dist) in targets.items():
            if path:
                print(f"🔹 Від {src} до {dest}: {path}, відстань = {dist}")