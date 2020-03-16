treasure_list = [[(3, 4), (2, 1), (3, 2), (4, 1), (2, 5)], [(1, 4), (4, 2), (4, 3), (1, 4), (3, 1)], [(5, 4), (4, 5), (5, 2), (4, 2), (2, 3)], [(3, 3), (1, 5), (5, 1), (3, 1), (3, 5)], [(2, 1), (5, 2), (3, 3), (1, 3), (2, 3)]]
start = ''


def treasure_search(treasure_list):
    row, col = treasure_list[0][0][0], treasure_list[0][0][1]

    while 1:
        if treasure_list[row-1][col-1][0] == row and treasure_list[row-1][col-1][1] == col:
            print(f'Treasure is in : row - {row} col - {col}')
            break
        else:
            tempRow = row
            row = treasure_list[tempRow-1][col-1][0]
            col = treasure_list[tempRow-1][col-1][1]
            # print(f'{row} & {col}')


treasure_search(treasure_list)

