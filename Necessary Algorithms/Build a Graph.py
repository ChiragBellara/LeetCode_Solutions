# IMPORTS
import math

edges = [
    [1, 2], [1, 3], [1, 4], [1, 5],
    [2, 3], [2, 4], [2, 5], [2, 6],
    [3, 4], [3, 5], [3, 6], [3, 7],
    [4, 5], [4, 6], [4, 7], [4, 8],
    [5, 6], [5, 7], [5, 8], [5, 9],
    [6, 7], [6, 8], [6, 9], [6, 10],
    [7, 8], [7, 9], [7, 10],
    [8, 9], [8, 10],
    [9, 10]
]

numEdges = 10
graph = {i: [] for i in range(1, numEdges + 1)}
graph_matrix = [[math.inf for _ in range(
    numEdges + 1)] for _ in range(numEdges + 1)]


# Adjacentcy List
def build_graph(edges):
    for edge in edges:
        # If it were a weighted graph, we would have used a tuple as the value
        # For eg. 0:[(1, 10), (2, 6)] implies that the edge from 0 to 1 has weight 10
        # and the edge from 0 to 2 has the weight 6
        graph[edge[0]].append(edge[1])

        # The next line should be removed it is was not an undirected graph
        graph[edge[1]].append(edge[0])


# Adjacentcy Matrix
def build_graph_matrix(edges):
    for u, v in edges:
        # For an unweighted graph, we simply assign the value as 1 for every edge
        # If it were a weighted graph, we would have assigned the respective weights
        # to each edge
        graph_matrix[u][v] = 1

        # The next line should be removed it is was not an undirected graph
        graph_matrix[v][u] = 1


if __name__ == "__main__":
    build_graph(edges)
    print(graph)
    print('\n\n\n')
    build_graph_matrix(edges)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in graph_matrix]))
