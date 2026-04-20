# astar.py

# A* Search Algorithm
# Uses cost + heuristic to find optimal path efficiently

import heapq

def astar(graph, heuristic, start, goal):
    open_list = []   # priority queue
    heapq.heappush(open_list, (0, start, [start]))

    g_cost = {start: 0}   # actual cost from start
    visited = set()
    nodes_visited = 0

    while open_list:
        f, current, path = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)
        nodes_visited += 1

        # Goal check
        if current == goal:
            return path, g_cost[current], nodes_visited

        # Explore neighbors
        for neighbor in graph[current]:
            cost = g_cost[current] + 1   # each edge cost = 1

            if neighbor not in g_cost or cost < g_cost[neighbor]:
                g_cost[neighbor] = cost
                f_value = cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_value, neighbor, path + [neighbor]))

    return [], 0, nodes_visited