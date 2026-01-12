"""
KRUSKAL's ALGORITHM to find MINIMUM SPANNING TREE

Logic:
	Sort based on weights
	Iterate edges
	If edges are not connected -> connect them (using Union Find) and add the weight to total

The idea is to connect the smallest weighing edges first and add their respecitve vertices to the same component
such that in the future if a bigger edge wants to connect those two vertices, it is not allowed to since the vertices
are already in the same component i.e. connected.
"""
class UnionFind:
	def __init__(self, size):
        self.parent = list(range(size))
    
    def _find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self._find(self.parent[node])
        return self.parent[node]
    
    def _union(self, p, q):
        parent_p = self._find(p)
        parent_q = self._find(q)
        
        if parent_p != parent_q:
            self.parent[parent_q] = parent_p
    
class Solution:
    def spanningTree(self, V, edges):
        # Kruskal's Algorithm
        uf = UnionFind(V)
        sorted_edges = sorted(edges, key = lambda x : x[2])
        total = 0
        
        for u, v, w in sorted_edges:
            component_u = uf._find(u)
            component_v = uf._find(v)
            
            if component_u != component_v:
                # Need to connect and add weight
                total += w
                uf._union(component_u, component_v)
        
        return total
