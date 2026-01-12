"""
PRIM's ALGORITHM to find the MINIMUM SPANNING TREE

Logic:
	Start at any node
	Add it to the min_heap
	Process the min_heap until it becomes empty
	Pop from the heap -> this popped node will be the smallest edge in the heap because ITS a MIN HEAP
	If this node is not visited yet, add it to visited and add it's edge weight to the total
	Iterate all it's neighbors and check if they are visited
	Any of the neighbors that are not visited, get added to the min_heap

IMPORTANT -> when adding to the min_heap, we add the value as (weight, node, parent) this ensures that the 
			 min_heap will always have the smallest weighing edge at the top.

"""

import heapq
class Solution:
    def spanningTree(self, V, edges):
        graph = {i: [] for i in range(V)}
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        visited = set()
        parent_list = [-1] * V
        total = 0
        
        min_heap = []
        # starting at V = 0
        # Add (edge_weight, destination_node, source_node) to the heap
        heapq.heappush(min_heap, (0, 0, -1))
        
        while min_heap:
            # pop the top most element -> this is guarenteed to be the smallest edge
            wt, node, parent = heapq.heappop(min_heap)
            
            # skip the node if it was visited earlier
            if node in visited:
                continue
            
            # process this destination if it is not visited yet
            total += wt
            visited.add(node)
            parent_list[node] = parent
            for nei, nei_wt in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (nei_wt, nei, node))
        
        return total
