class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state  
        self.parent = parent  
        self.move = move  
        self.h_cost = self.calculate_heuristic()

    def calculate_heuristic(self):
        goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        h = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_x, goal_y = divmod(self.state[i][j] - 1, 3)
                    h += abs(i - goal_x) + abs(j - goal_y)
        return h

    def generate_children(self):
        children = []
        zero_pos = [(i, j) for i in range(3) for j in range(3) if self.state[i][j] == 0][0]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        for direction in directions:
            new_zero_pos = (zero_pos[0] + direction[0], zero_pos[1] + direction[1])
            if 0 <= new_zero_pos[0] < 3 and 0 <= new_zero_pos[1] < 3:
                new_state = [row[:] for row in self.state] 
                new_state[zero_pos[0]][zero_pos[1]], new_state[new_zero_pos[0]][new_zero_pos[1]] = (
                    new_state[new_zero_pos[0]][new_zero_pos[1]], new_state[zero_pos[0]][zero_pos[1]]
                )
                children.append(Node(new_state, self, f"Move {new_state[new_zero_pos[0]][new_zero_pos[1]]}"))
        return children

class GreedyBestFirstSearch:
    def __init__(self, start_state):
        self.start_state = start_state
        self.goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

    def solve(self):
        open_list = [Node(self.start_state)]
        closed_list = set()

        while open_list:
            open_list.sort(key=lambda node: node.h_cost)
            current_node = open_list.pop(0)  

            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)

            closed_list.add(tuple(map(tuple, current_node.state)))  
            for child in current_node.generate_children():
                if tuple(map(tuple, child.state)) not in closed_list:
                    open_list.append(child)

        return None  

    def trace_solution(self, node):
        path = []
        while node is not None:
            path.append(node.state)
            node = node.parent
        return path[::-1]  

start_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

gbfs = GreedyBestFirstSearch(start_state)
solution_path = gbfs.solve()

for step in solution_path:
    for row in step:
        print(row)
    print() 
