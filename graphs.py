def bfs(graph, start):
    visited = []
    queue = [start]
    
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            print(vertex)  # Process the node
            queue.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(graph, 'A')


def dfs(graph, start, visited):
    visited.append(start)
    print(start)  # Process the node
    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited = []
dfs(graph, 'A', visited)


def iddfs(graph, start, goal):
    def dls(node, depth):
        if depth == 0:
            return node == goal
        if depth > 0:
            for neighbor in graph.get(node, []):
                if dls(neighbor, depth - 1):
                    return True
        return False

    depth = 0
    while True:
        if dls(start, depth):
            return True
        depth += 1

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(iddfs(graph, 'A', 'F'))  # Output: True


def a_star(graph, start, goal, h):
    open_list = [(start, 0)]
    closed_list = []
    g = {start: 0}
    parents = {start: None}

    while open_list:
        current, _ = min(open_list, key=lambda x: x[1])
        open_list = [node for node in open_list if node[0] != current]

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        closed_list.append(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue
            tentative_g = g[current] + cost
            if neighbor not in [node[0] for node in open_list] or tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                f = tentative_g + h(neighbor, goal)
                open_list.append((neighbor, f))
                parents[neighbor] = current

    return None

# Example usage:
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 1), ('E', 5)],
    'C': [('A', 3), ('F', 2)],
    'D': [('B', 1)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 2), ('E', 1)]
}

def heuristic(node, goal):
    heuristics = {'A': 6, 'B': 5, 'C': 2, 'D': 4, 'E': 1, 'F': 0}
    return heuristics[node]

print(a_star(graph, 'A', 'F', heuristic))  # Output: ['A', 'C', 'F']


def greedy_bfs(graph, start, goal, h):
    open_list = [(start, h(start, goal))]
    closed_list = []
    parents = {start: None}

    while open_list:
        current, _ = min(open_list, key=lambda x: x[1])
        open_list = [node for node in open_list if node[0] != current]

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        closed_list.append(current)

        for neighbor, cost in graph[current]:
            if neighbor not in closed_list and neighbor not in [node[0] for node in open_list]:
                open_list.append((neighbor, h(neighbor, goal)))
                parents[neighbor] = current

    return None

# Example usage:
print(greedy_bfs(graph, 'A', 'F', heuristic))  # Output: ['A', 'C', 'F']
