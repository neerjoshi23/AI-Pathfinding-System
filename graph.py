# graph.py

# Graph representation using adjacency list (dictionary)
# Each node maps to its neighboring nodes

def get_graph():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E', 'F'],
        'C': ['A', 'D', 'F'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['B', 'D', 'F'],
        'F': ['B', 'C', 'D', 'E']
    }
    return graph


# Heuristic values for A* (given in lab manual)
def get_heuristic():
    h = {
        'A': 7,
        'B': 6,
        'C': 4,
        'D': 2,
        'E': 0,
        'F': 3   # extra node (you can assign reasonable value)
    }
    return h