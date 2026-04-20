from graph import get_graph
from dfs import dfs
from bfs import bfs

graph = get_graph()

start = 'A'
goal = 'E'

path, nodes = dfs(graph, start, goal)

print("DFS Path:", " → ".join(path))
print("Nodes Visited:", nodes)

bfs_path, bfs_nodes = bfs(graph, start, goal)

print("\nBFS Path:", " → ".join(bfs_path))
print("Nodes Visited:", bfs_nodes)