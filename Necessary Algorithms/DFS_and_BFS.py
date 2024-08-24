# DFS and BFS Algorithms

# IMPORTS
from collections import deque


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


# DFS -- Depth First Search
visited_DFS = set()
outcome_DFS = []


def DFS(node):
    if node not in visited_DFS:
        visited_DFS.add(node)
        outcome_DFS.append(node)

    for neighbour in graph[node]:
        DFS(neighbour)


# BFS -- Breadth First Search
visited_BFS = set()
outcome_BFS = []


def BFS(node):
    que = deque()

    visited_BFS.add(node)
    outcome_BFS.append(node)
    que.append(node)

    while que:
        v = que.popleft()
        for neighbour in graph[v]:
            if neighbour not in visited_BFS:
                visited_BFS.add(neighbour)
                outcome_BFS.append(neighbour)
                que.append(neighbour)


# DRIVER Code
if __name__ == "__main__":
    DFS('5')
    print(outcome_DFS)

    BFS('5')
    print(outcome_BFS)
