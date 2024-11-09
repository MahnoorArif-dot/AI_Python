class AlphaBetaPruning:
    def __init__(self, depth, game_state, player):
        self.depth = depth
        self.game_state = game_state
        self.player = player
        self.evaluated_nodes = 0

    def is_terminal(self, state):
        win_conditions = [
            [state[0], state[1], state[2]],
            [state[3], state[4], state[5]],
            [state[6], state[7], state[8]],
            [state[0], state[3], state[6]],
            [state[1], state[4], state[7]],
            [state[2], state[5], state[8]],
            [state[0], state[4], state[8]],
            [state[2], state[4], state[6]]
        ]
        if ['X', 'X', 'X'] in win_conditions or ['O', 'O', 'O'] in win_conditions:
            return True
        if '-' not in state:
            return True
        return False

    def utility(self, state):
        win_conditions = [
            [state[0], state[1], state[2]],
            [state[3], state[4], state[5]],
            [state[6], state[7], state[8]],
            [state[0], state[3], state[6]],
            [state[1], state[4], state[7]],
            [state[2], state[5], state[8]],
            [state[0], state[4], state[8]],
            [state[2], state[4], state[6]]
        ]
        if ['X', 'X', 'X'] in win_conditions:
            return 1
        if ['O', 'O', 'O'] in win_conditions:
            return -1
        return 0

    def alphabeta(self, state, depth, alpha, beta, maximizing_player):
        self.evaluated_nodes += 1
        if depth == 0 or self.is_terminal(state):
            return self.utility(state)

        if maximizing_player:
            max_eval = float('-inf')
            for child in self.get_children(state):
                eval = self.alphabeta(child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for child in self.get_children(state):
                eval = self.alphabeta(child, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def best_move(self, state):
        best_value = float('-inf')
        best_move = None
        for move in self.get_children(state):
            move_value = self.alphabeta(move, self.depth - 1, float('-inf'), float('inf'), False)
            if move_value > best_value:
                best_value = move_value
                best_move = move
        return best_move, self.evaluated_nodes

    def get_children(self, state):
        children = []
        for i in range(len(state)):
            if state[i] == '-':
                new_state = state[:]
                new_state[i] = 'X' if self.player == 'X' else 'O'
                children.append(new_state)
        return children

initial_state = ['-', '-', '-', '-', '-', 'O', '-', '-', '-']
ab_pruning = AlphaBetaPruning(depth=3, game_state=initial_state, player='X')
best_move, evaluated_nodes = ab_pruning.best_move(initial_state)
print("Best Move:", best_move)
print("Evaluated Nodes:", evaluated_nodes)


