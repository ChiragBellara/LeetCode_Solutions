"""
Formal Problem Statement

You are given a directed graph where each vertex is represented by the following structure:

Node {
    label: string
    connections: List<Node>   // outgoing edges
    hasIPAddress: boolean
}


Each directed edge in the graph goes from a node to every node in its connections list. Some nodes are marked with hasIPAddress = true, indicating that they contain a valid IP address.

Goal:
Design an algorithm that returns the set of all nodes from which it is possible to reach at least one node with hasIPAddress = true by following the directed edges of the graph.

Your solution must handle arbitrary graph topology, including cycles, disconnected components, and multiple IP-address nodes. Analyze the time and space complexity of your approach.
"""

from collections import defaultdict, deque

class Node:
    def __init__(self, label, hasIPAddress = False):
        self.label = label
        self.connections = []
        self.hasIPAddress = hasIPAddress
    
    def __repr__(self):
        return self.label

def build_reverse_map(all_nodes):
    reversed_adj = defaultdict(list)
    for node in all_nodes:
        for nei in node.connections:
            reversed_adj[nei].append(node)
    
    return reversed_adj

def node_that_can_read_an_ip(reversed_adj, all_nodes):
    # Multi Node BFS
    que = deque()
    reacheable = set()

    for node in all_nodes:
        if node.hasIPAddress:
            que.append(node)
            reacheable.add(node)
    
    while que:
        current = que.popleft()
        for prev in reversed_adj[current]:
            if prev not in reacheable:
                reacheable.add(prev)
                que.append(prev)
    
    return list(reacheable)[::-1]
