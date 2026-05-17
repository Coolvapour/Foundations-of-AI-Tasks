# Unit: CCS 2226 Foundations of AI
# Student Name: Moses Kiprono Leleito
# Registration Number: CIT-227-073/2024
# Task: Practical Task Four - Breadth First Search (BFS) and Depth First Search (DFS)

from collections import deque

# Defining the graph based on nodes and their connections
# We use a dictionary where keys are nodes and values are lists of neighbors
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['Goal'],
    'E': ['Goal'],
    'F': [],
    'Goal': []
}

def bfs(graph, start, goal):
    """Implementation of Breadth-First Search to find the path."""
    queue = deque([[start]])
    visited = {start}
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
            
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

def dfs(graph, start, goal):
    """Implementation of Depth-First Search to find the path."""
    stack = [[start]]
    visited = {start}
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node == goal:
            return path
            
        # We visit neighbors in reverse to maintain standard DFS order
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None

if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'Goal'
    
    print(f"--- Search Path Analysis: {start_node} to {goal_node} ---")
    
    # Executing BFS
    result_bfs = bfs(graph, start_node, goal_node)
    print(f"BFS Path: {' -> '.join(result_bfs) if result_bfs else 'No path found'}")
    
    # Executing DFS
    result_dfs = dfs(graph, start_node, goal_node)
    print(f"DFS Path: {' -> '.join(result_dfs) if result_dfs else 'No path found'}")