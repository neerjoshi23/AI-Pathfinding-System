# dfs.py

# Depth First Search implementation
# Explores nodes deeply before backtracking

def dfs(graph, start, goal):
    visited = set()        # to keep track of visited nodes
    path = []              # to store current path
    nodes_visited = 0      # counter

    def dfs_helper(node):
        nonlocal nodes_visited

        visited.add(node)
        path.append(node)
        nodes_visited += 1

        # If goal is found, stop
        if node == goal:
            return True

        # Explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_helper(neighbor):
                    return True

        # Backtrack if not found
        path.pop()
        return False

    dfs_helper(start)

    return path, nodes_visited