import math

original_string = 'ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'

rows = math.ceil(math.sqrt(len(original_string)))
print(rows)
cols = math.ceil(len(original_string) / rows)
list_l, final_matrix = [], []
i = 0
for col in range(0, cols):
    for row in range(0, rows):
        if i < len(original_string):
            list_l.append(original_string[i])
            i += 1
        else:
            list_l.append(' ')
    final_matrix.append(list_l)
    list_l = []
print(final_matrix)
str = ''
for col in range(0, rows):
    for row in range(0, cols):
        str += final_matrix[row][col]
    str += ' '
print(f'Original Message : {original_string}')
print(f'Encoded Message : {str}')


