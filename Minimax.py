class Minimax:
    def __init__(self, game_state):
        self.game_state = game_state

    def is_terminal(self, state):
        for row in state:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return True
        
        for col in range(3):
            if state[0][col] == state[1][col] == state[2][col] and state[0][col] != " ":
                return True
        
        if state[0][0] == state[1][1] == state[2][2] and state[0][0] != " ":
            return True
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] != " ":
            return True

        if all(cell != " " for row in state for cell in row):
            return True
        
        return False

    def utility(self, state):
        for row in state:
            if row[0] == row[1] == row[2]:
                if row[0] == "X":
                    return 1
                elif row[0] == "O":
                    return -1
        
        for col in range(3):
            if state[0][col] == state[1][col] == state[2][col]:
                if state[0][col] == "X":
                    return 1
                elif state[0][col] == "O":
                    return -1
        
        if state[0][0] == state[1][1] == state[2][2]:
            if state[0][0] == "X":
                return 1
            elif state[0][0] == "O":
                return -1
        if state[0][2] == state[1][1] == state[2][0]:
            if state[0][2] == "X":
                return 1
            elif state[0][2] == "O":
                return -1

        return 0  

    def minimax(self, state, depth, maximizing_player):
        if self.is_terminal(state):
            return self.utility(state)

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == " ":
                        state[i][j] = "X" 
                        eval = self.minimax(state, depth + 1, False)
                        state[i][j] = " "  
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == " ":
                        state[i][j] = "O"  
                        eval = self.minimax(state, depth + 1, True)
                        state[i][j] = " "  
                        min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, state):
        best_eval = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if state[i][j] == " ":
                    state[i][j] = "X"  
                    eval = self.minimax(state, 0, False)
                    state[i][j] = " " 
                    if eval > best_eval:
                        best_eval = eval
                        best_move = (i, j)
        return best_move

if __name__ == "__main__":
    board = [
        ["X", "X", " "],
        ["X", "O", "X"],
        ["O", " ", " "]
    ]

    minimax = Minimax(board)
    move = minimax.best_move(board)
    if move:
        print(f"Best move for X: {move}")
    else:
        print("No valid moves available.")
