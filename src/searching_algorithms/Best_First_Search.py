import heapq

def best_first_search(game):
    open_set = []
    heapq.heappush(open_set, (heuristic(game), game))
    f_score = {game:heuristic(game)}

    while open_set:
        current_state = heapq.heappop(open_set)[1]

        if current_state.is_goal_state():
            return extract_path(current_state)
        
        next_states = current_state.generate_next_states()

        for next_state in next_states:
            if next_state not in f_score or heuristic(next_state) < f_score[next_state]:
                f_score[next_state] = heuristic(next_state)
                if next_state not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[next_state], next_state))
    return None

def heuristic(game):
    return game.chess_board.count_NumberOfPieces() - 1

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