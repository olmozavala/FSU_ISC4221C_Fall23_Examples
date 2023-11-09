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
plt.figure(figsize=(4, 4))
nx.draw(G, with_labels=True)
plt.title('Example Graph')
plt.show()

# %% ------- Implementing the path algorithm -------

def get_idx(v_str, letter):
    return np.where(v_str == letter)[0][0]

# Simple dictionary from letters to numbers. From A to H
v_str = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
edges_str = ('AD','AF','EF','DE','BC','CH')
edges = [[np.where(v_str == letter)[0][0] for letter in edge] for edge in edges_str]
print(f'Edges {edges_str}')
print(f'Edges by index: {edges}')

def find_path(edges, n_vertices, node_a, node_b):
    # Step one initialize
    n_vertex = len(edges)
    used = np.zeros(n_vertex, dtype=np.uint8)
    new = np.zeros(n_vertex, dtype=np.uint8)
    untouched = np.ones(n_vertex, dtype=np.uint8)

    new[node_a] = 1
    untouched[node_a] = 0

find_path(edges, range(len(v_str)), get_idx(v_str, 'A'),  get_idx(v_str, 'H'))


# %% ------- Implementing the path algorithm -------
def get_idx(v_str, letter):
    return np.where(v_str == letter)[0][0]

# Simple dictionary from letters to numbers. From A to H
v_str = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
edges_str = ('AD','AF','EF','DE','BC','CH')
edges = [[np.where(v_str == letter)[0][0] for letter in edge] for edge in edges_str]
print(f'Edges {edges_str}')
print(f'Edges by index: {edges}')

def find_path(edges, node_a, node_b):
    # Step one initialize
    n_vertex = len(edges)
    used = np.zeros(n_vertex, dtype=np.uint8)
    new = np.zeros(n_vertex, dtype=np.uint8)
    untouched = np.ones(n_vertex, dtype=np.uint8)

    new[node_a] = 1
    untouched[node_a] = 0

    while np.sum(new) > 0:
        # Step two Move item from new into used, call it S
        S = np.where(new == 1)[0][0]
        print(f'------------ Analizing node {v_str[S]}')
        new[S] = 0
        used[S] = 1

        # For each edge which uses S (T). Verify is not equal to node_b, if so return True
        for edge in edges:
            if S in edge:
                T = edge[0] if edge[0] != S else edge[1]
                print(f'--- Analizing edge {v_str[S]}-{v_str[T]}')
                if T == node_b:
                    print('\n Found path')
                    return True
                else:
                    #  Otherwise, if T is in untouched, move it to new 
                    if untouched[T]:
                        new[T] = 1
                        untouched[T] = 0
                # Print the state of used, new and untouched
                print(f'Used: {used}')
                print(f'New: {new}')
                print(f'Untouched: {untouched}')
    
    print('\n No path found')
    return False
    

find_path(edges, get_idx(v_str, 'A'),  get_idx(v_str, 'H'))

