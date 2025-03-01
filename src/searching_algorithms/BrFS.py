from collections import deque

def brfs(game):
    queue = deque([game])
    visited = []

    while queue:
        current_state = queue.popleft()
        visited.append(current_state)
        if current_state.is_goal_state():
            return (extract_path(current_state), visited)
    
        

        next_states = current_state.generate_next_states()

        for state in next_states:
            if state not in visited and state not in queue:
                queue.append(state)

    return ([], [])

def extract_path(goal_state):
    path = []
    current_state = goal_state
    while current_state.parent is not None:
        path += [(current_state.move)]
        current_state = current_state.parent
    path.reverse()
    chess_path = array_to_chess_coordinates(path)

    return chess_path

def array_to_chess_coordinates(array_coords):
    chess_coords = []
    for x, y, z, t in array_coords:
        old_row = 8 - x
        old_column = chr(y + 97)  # Chuyển cột từ số sang chữ

        new_row = 8 - z
        new_column = chr(t + 97)  # Chuyển cột từ số sang chữ
        chess_coords.append(f"{old_column}{old_row}{new_column}{new_row}")
    return chess_coords
