# %%
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# %%

# Define the connections as a list of edges
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')]
isolated_nodes = ['E']


# Create an empty graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from(edges)
G.add_nodes_from(isolated_nodes)

# Draw the graph
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True)
plt.title('Example Graph')
plt.show()

# %%

# %% Adjacency list representation of the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# edge_list = [(edges[key],y) for y in graph[key] for key in graph.keys()]
edge_list = [(key,edge_y) for key in graph.keys() for y in graph[key] for edge_y in y ]
print(edge_list)

# Create an empty graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from(edge_list)

# Draw the graph
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True)
plt.title('Example Graph')
plt.show()
# %%%
def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

visited = set()  # A set to keep track of visited nodes

dfs_recursive(graph, 'D', visited)

# %%
import heapq

def dijkstra(graph, start):
    # Initialize distances and predecessors
    distances = {node: float('infinity') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0
    
    # Priority queue to store (distance, node) pairs
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if this node has already been processed
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Check if a shorter path to neighbor exists
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, predecessors

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances, predecessors = dijkstra(graph, 'A')
print("Shortest distances:", distances)
print("Predecessors:", predecessors)

# %%
