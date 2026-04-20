# bfs.py

# Breadth First Search implementation
# Explores nodes level by level and guarantees shortest path

from collections import deque

def bfs(graph, start, goal):
    visited = set()                # track visited nodes
    queue = deque([[start]])       # queue stores paths
    nodes_visited = 0

    while queue:
        path = queue.popleft()     # get first path
        node = path[-1]

        if node not in visited:
            visited.add(node)
            nodes_visited += 1

            # If goal is found
            if node == goal:
                return path, nodes_visited

            # Add neighbors to queue
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return [], nodes_visited