from graph import get_graph, get_heuristic
from dfs import dfs
from bfs import bfs
from astar import astar

graph = get_graph()
heuristic = get_heuristic()

start = 'A'
goal = 'E'

# Run all algorithms
dfs_path, dfs_nodes = dfs(graph, start, goal)
bfs_path, bfs_nodes = bfs(graph, start, goal)
astar_path, astar_cost, astar_nodes = astar(graph, heuristic, start, goal)

# Store results
results = {
    "DFS": {
        "path": dfs_path,
        "cost": "-",
        "nodes": dfs_nodes
    },
    "BFS": {
        "path": bfs_path,
        "cost": "-",
        "nodes": bfs_nodes
    },
    "A*": {
        "path": astar_path,
        "cost": astar_cost,
        "nodes": astar_nodes
    }
}

# ----- PATH RESULTS -----
print("Start Node:", start)
print("Goal Node:", goal)

print("\n----- PATH RESULTS -----")

print("\nDFS Path:", " → ".join(dfs_path))
print("Nodes Visited:", dfs_nodes)

print("\nBFS Path:", " → ".join(bfs_path))
print("Nodes Visited:", bfs_nodes)

print("\nA* Path:", " → ".join(astar_path))
print("Cost:", astar_cost)
print("Nodes Visited:", astar_nodes)

# ----- COMPARISON TABLE -----
print("\n----- COMPARISON TABLE -----")
print("Algorithm   Path            Cost   Nodes Visited")
print("------------------------------------------------")

for algo in results:
    path_str = "→".join(results[algo]["path"])
    cost = results[algo]["cost"]
    nodes = results[algo]["nodes"]

    print(f"{algo:<10} {path_str:<15} {cost:<6} {nodes}")

# ----- BEST ALGORITHM -----
# Choose based on least nodes visited (efficiency)
best_algo = min(results, key=lambda x: results[x]["nodes"])

print("\n----- ANALYSIS -----")
print(f"Best Algorithm: {best_algo}")

print("Reason:")
print(f"- Least nodes visited = {results[best_algo]['nodes']}")

if results[best_algo]["cost"] != "-":
    print(f"- Minimum cost = {results[best_algo]['cost']}")