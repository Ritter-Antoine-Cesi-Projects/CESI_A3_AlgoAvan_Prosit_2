import time
import random

Graph_1 = {
    "A" : {"B": 1, "C": 5, "D": 6},
    "B" : {"A": 1, "C": 3, "D": 4},
    "C" : {"A": 5, "B": 3, "D": 2},
    "D" : {"A": 6, "B": 4, "C": 2}
}

Graph_2 = {
    "A" : {"B": 1, "C": 4.5, "D": 5, "E": 4, "F": 2.4, "G": 2.2},
    "B" : {"A": 1, "C": 4, "D": 4.5, "E": 4.7, "F": 3.4, "G": 3.2},
    "C" : {"A": 4.5, "B": 4, "D": 2, "E": 5.1, "F": 5.8, "G": 5.9},
    "D" : {"A": 5, "B": 4.5, "C": 2, "E": 3.5, "F": 5, "G": 5.2},
    "E" : {"A": 4, "B": 4.7, "C": 5.1, "D": 3.5, "F": 2.6, "G": 2.7},
    "F" : {"A": 2.4, "B": 3.4, "C": 5.8, "D": 5, "E": 2.6, "G": 0.3},
    "G" : {"A": 2.2, "B": 3.2, "C": 5.9, "D": 5.2, "E": 2.7, "F": 0.3}
}

Graph_3 = {
    "A": {"B": 1, "C": 4.5, "D": 5, "E": 4, "F": 2.4, "G": 2.2, "H": 3.1, "I": 4.6},
    "B": {"A": 1, "C": 4, "D": 4.5, "E": 4.7, "F": 3.4, "G": 3.2, "H": 3.6, "I": 4.3},
    "C": {"A": 4.5, "B": 4, "D": 2, "E": 5.1, "F": 5.8, "G": 5.9, "H": 4.3, "I": 3.9},
    "D": {"A": 5, "B": 4.5, "C": 2, "E": 3.5, "F": 5, "G": 5.2, "H": 4.6, "I": 3.8},
    "E": {"A": 4, "B": 4.7, "C": 5.1, "D": 3.5, "F": 2.6, "G": 2.7, "H": 2.9, "I": 4.1},
    "F": {"A": 2.4, "B": 3.4, "C": 5.8, "D": 5, "E": 2.6, "G": 0.3, "H": 2.1, "I": 3.5},
    "G": {"A": 2.2, "B": 3.2, "C": 5.9, "D": 5.2, "E": 2.7, "F": 0.3, "H": 1.9, "I": 3.2},
    "H": {"A": 3.1, "B": 3.6, "C": 4.3, "D": 4.6, "E": 2.9, "F": 2.1, "G": 1.9, "I": 4.5},
    "I": {"A": 4.6, "B": 4.3, "C": 3.9, "D": 3.8, "E": 4.1, "F": 3.5, "G": 3.2, "H": 4.5}
}

Graph_4 = {
    "A": {"B": 1, "C": 4.5, "D": 5, "E": 4, "F": 2.4, "G": 2.2, "H": 3.1, "I": 4.6, "J": 3.9},
    "B": {"A": 1, "C": 4, "D": 4.5, "E": 4.7, "F": 3.4, "G": 3.2, "H": 3.6, "I": 4.3, "J": 3.7},
    "C": {"A": 4.5, "B": 4, "D": 2, "E": 5.1, "F": 5.8, "G": 5.9, "H": 4.3, "I": 3.9, "J": 2.5},
    "D": {"A": 5, "B": 4.5, "C": 2, "E": 3.5, "F": 5, "G": 5.2, "H": 4.6, "I": 3.8, "J": 3.4},
    "E": {"A": 4, "B": 4.7, "C": 5.1, "D": 3.5, "F": 2.6, "G": 2.7, "H": 2.9, "I": 4.1, "J": 4.5},
    "F": {"A": 2.4, "B": 3.4, "C": 5.8, "D": 5, "E": 2.6, "G": 0.3, "H": 2.1, "I": 3.5, "J": 4.2},
    "G": {"A": 2.2, "B": 3.2, "C": 5.9, "D": 5.2, "E": 2.7, "F": 0.3, "H": 1.9, "I": 3.2, "J": 3.6},
    "H": {"A": 3.1, "B": 3.6, "C": 4.3, "D": 4.6, "E": 2.9, "F": 2.1, "G": 1.9, "I": 4.5, "J": 4.1},
    "I": {"A": 4.6, "B": 4.3, "C": 3.9, "D": 3.8, "E": 4.1, "F": 3.5, "G": 3.2, "H": 4.5, "J": 3.3},
    "J": {"A": 3.9, "B": 3.7, "C": 2.5, "D": 3.4, "E": 4.5, "F": 4.2, "G": 3.6, "H": 4.1, "I": 3.3}
}

def generate_random_graph(num_vertices, max_edge_weight):
    vertices = [i for i in range(num_vertices)]
    graph = {vertex: {} for vertex in vertices}

    for vertex in vertices:
        for other_vertex in vertices:
            if vertex != other_vertex and other_vertex not in graph[vertex]:
                weight = random.randint(1, max_edge_weight)
                graph[vertex][other_vertex] = weight
                graph[other_vertex][vertex] = weight

    return graph

def find_closest_vertex(graph, vertices, clusters):
    min_distance = float('inf')
    min_edge = None
    min_cluster = None
    for vertex in vertices:
        for cluster in clusters:
            for end_vertex in [cluster[0], cluster[-1]]:
                if graph[vertex][end_vertex] < min_distance:
                    min_distance = graph[vertex][end_vertex]
                    min_edge = (vertex, end_vertex)
                    min_cluster = cluster
    return min_edge, min_cluster

def add_vertex_to_cluster(min_edge, min_cluster, vertices):
    if min_edge[1] == min_cluster[0]:
        min_cluster.insert(0, min_edge[0])
    else:
        min_cluster.append(min_edge[0])
    vertices.remove(min_edge[0])

def find_next_cluster(graph, path, clusters):
    return min(clusters, key=lambda cluster: min(graph[path[-1]][cluster[0]], graph[path[-1]][cluster[-1]]))

def add_cluster_to_path(graph, path, clusters):
    next_cluster = find_next_cluster(graph, path, clusters)
    if graph[path[-1]][next_cluster[0]] < graph[path[-1]][next_cluster[-1]]:
        path += next_cluster
    else:
        path += next_cluster[::-1]
    clusters.remove(next_cluster)

def algorithm(graph, start_node):
    vertices = list(graph.keys())
    clusters = [[vertices.pop(0)]]
    while vertices:
        min_edge, min_cluster = find_closest_vertex(graph, vertices, clusters)
        add_vertex_to_cluster(min_edge, min_cluster, vertices)
    path = clusters.pop(0)
    while clusters:
        add_cluster_to_path(graph, path, clusters)
    path = path[path.index(start_node):] + path[:path.index(start_node)] + [start_node]
    return path

def path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        cost += graph[current_node][next_node]
    return cost

def main():
    num_vertices = 10000
    max_edge_weight = 10
    start_node = 0

    graph = generate_random_graph(num_vertices, max_edge_weight)
    print("Graph generated")

    start_time = time.time()
    mst = algorithm(graph, start_node)
    end_time = time.time()
    print("End of algorithm")
    cost = path_cost(graph, mst)

    print(f"Path: {mst}")
    print(f"Cost: {cost}")
    print(f"Execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()