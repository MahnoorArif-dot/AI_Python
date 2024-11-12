def dfs(graph, start, visited=None):
    if visited is None:
        visited = [] 
    visited.append(start)  
    print(start, end=" ") 
    
    for neighbor in graph[start]:  
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  

graph = {
    1: [3, 4],
    2: [2, 4], 
    3: [0, 2, 4],  
    4: [1, 5],
    5: [6],
    6: [], 
    0: []   
}

start_node = 1 
dfs(graph, start_node)  

