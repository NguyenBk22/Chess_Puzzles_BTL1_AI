from collections import deque

def brfs(game):
    queue = deque([game])
    visited = set()

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal_state():
            return current_state.chess_board
    
        visited.add(current_state)

        next_states = current_state.generate_next_states()

        for state in next_states:
            if state not in visited and state not in queue:
                queue.append(state)
                print(state.chess_board)

    return None

        