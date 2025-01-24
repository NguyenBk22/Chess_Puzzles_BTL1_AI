
def load_initial_position(filename):
    positions = []

    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            piece = line[0]
            pos = line[1:].strip()
            positions.append( (piece, pos))

    return positions