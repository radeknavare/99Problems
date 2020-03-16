chess_pos = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

black_queen = [4, 2]
white_queen = [5, 1]


def queen_attack(black_queen, white_queen):
    if black_queen[0] == black_queen[1] and white_queen[0] == white_queen[1] or black_queen[0] == white_queen[1] and black_queen[1] == white_queen[0]:
        return True
    if black_queen[0] == white_queen[0]:
        return True
    if black_queen[1] == white_queen[1]:
        return True

print(queen_attack(black_queen, white_queen))
