from graph import get_graph
from dfs import dfs
from bfs import bfs
from astar import astar
from graph import get_heuristic

graph = get_graph()

start = 'A'
goal = 'E'

path, nodes = dfs(graph, start, goal)

print("DFS Path:", " → ".join(path))
print("Nodes Visited:", nodes)

bfs_path, bfs_nodes = bfs(graph, start, goal)

print("\nBFS Path:", " → ".join(bfs_path))
print("Nodes Visited:", bfs_nodes)

heuristic = get_heuristic()

astar_path, astar_cost, astar_nodes = astar(graph, heuristic, start, goal)

print("\nA* Path:", " → ".join(astar_path))
print("Cost:", astar_cost)
print("Nodes Visited:", astar_nodes)