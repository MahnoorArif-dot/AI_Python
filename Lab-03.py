class PuzzleNode:
    def __init__(self, state, parent, move, g_cost, h_cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost  
        self.h_cost = h_cost  
        self.f_cost = g_cost + h_cost  
    
    def generate_children(self):
        children = []
        empty_index = self.state.index(0) 
        
        
        possible_moves = {
            'up': -3,   
            'down': 3,
            'left': -1,
            'right': 1
        }
        
        for move, position_change in possible_moves.items():
            new_index = empty_index + position_change
            if 0 <= new_index < len(self.state):
                if (move == 'left' and empty_index % 3 == 0) or (move == 'right' and empty_index % 3 == 2):
                    continue
                new_state = list(self.state)
                new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
                child_node = PuzzleNode(state=new_state, parent=self, move=move, g_cost=self.g_cost + 1, h_cost=0)
                children.append(child_node)
        
        return children
    
    def calculate_heuristic(self, goal_state):
        h = 0
        for i in range(1, len(self.state)):
            current_pos = self.state.index(i)
            goal_pos = goal_state.index(i)
            h += abs(current_pos % 3 - goal_pos % 3) + abs(current_pos // 3 - goal_pos // 3)
        return h


class AStarSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.open_list = []  
        self.closed_list = [] 
    
    def solve(self):
        start_node = PuzzleNode(state=self.start_state, parent=None, move=None, g_cost=0, h_cost=0)
        start_node.h_cost = start_node.calculate_heuristic(self.goal_state)
        self.open_list.append(start_node)
        
        while self.open_list:
            self.open_list.sort(key=lambda node: node.f_cost)
            current_node = self.open_list.pop(0)
            self.closed_list.append(current_node)
            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)
        
            for child in current_node.generate_children():
                if any(child.state == closed_child.state for closed_child in self.closed_list):
                    continue
                
                child.h_cost = child.calculate_heuristic(self.goal_state)
                existing_node = next((node for node in self.open_list if node.state == child.state), None)
                if existing_node and child.g_cost >= existing_node.g_cost:
                    continue
                self.open_list.append(child)
        
        return None 
    
    def trace_solution(self, node):
        solution_path = []
        current_node = node
        while current_node:
            solution_path.append(current_node.move)
            current_node = current_node.parent
        solution_path.reverse()  
        return solution_path[1:] 
    
    def is_solvable(self, state):
        inversions = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] and state[j] and state[i] > state[j]:
                    inversions += 1
        return inversions % 2 == 0
start = [1, 2, 3, 4, 5, 6, 7, 8, 0] 
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]  

solver = AStarSolver(start_state=start, goal_state=goal)
if solver.is_solvable(start):
    solution = solver.solve()
    print("Solution path:", solution)
else:
    print("This puzzle is not solvable.")
