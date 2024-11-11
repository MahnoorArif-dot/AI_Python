class PuzzleNode:
    def __init__(self, state, parent, move, depth):
        self.state = state
        self.parent = parent
        self.move = move 
        self.depth = depth  
    
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
                child_node = PuzzleNode(state=new_state, parent=self, move=move, depth=self.depth + 1)
                children.append(child_node)
        
        return children

    def trace_solution(self):
        
        solution = []
        current_node = self
        while current_node:
            solution.append(current_node.move)
            current_node = current_node.parent
        solution.reverse() 
        return solution[1:]  


class IDFSSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
    
    def dfs(self, node, depth_limit):
        if node.state == self.goal_state:
            return node

        if node.depth >= depth_limit:
            return None
        
        for child in node.generate_children():
            result = self.dfs(child, depth_limit)
            if result:
                return result
        
        return None
    
    def iddfs(self):
        depth_limit = 0
        while True:
            root = PuzzleNode(state=self.start_state, parent=None, move=None, depth=0)
            result = self.dfs(root, depth_limit)
            if result:
                return result.trace_solution()
            depth_limit += 1

    def is_solvable(self, state):
        inversions = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] and state[j] and state[i] > state[j]:
                    inversions += 1
        return inversions % 2 == 0

start = [1, 2, 3, 4, 5, 6, 0, 7, 8]  
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]  

solver = IDFSSolver(start_state=start, goal_state=goal)

if solver.is_solvable(start):
    solution = solver.iddfs()
    print("Solution path:", solution)
else:
    print("This puzzle is not solvable.")
