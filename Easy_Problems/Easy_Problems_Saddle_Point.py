treasure_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(treasure_list)
cols = len(treasure_list[0])


def check_saddle(value, row, col):
    rflag, cflag = 0, 0
    for icol in range(0, cols):
        if col == icol:
            continue
        elif value < treasure_list[row][icol]:
            rflag = 1
        else:
            rflag = 0
            break
    for irow in range(0, rows):
        if row == irow:
            continue
        elif value > treasure_list[irow][col]:
            cflag = 1
        else:
            cflag = 0
            break
    return rflag + cflag


for row in range(0, rows):
    for col in range(0, cols):
        value = treasure_list[row][col]
        if check_saddle(value, row, col) == 2:
            print(f'({row},{col})')
