import math

f = open("Mayor.txt", "r")
table = []
for line in f:
    table.append(line.replace('\n', '').split('\t'))
total_rows = len(table)
total_cols = len(table[0])
count, total_votes_list = 0, []
total_votes = 0
for col in range(1, total_cols):
    for row in range(0, total_rows):
        count += int(table[row][col])
    total_votes_list.append(count)
    total_votes += count
    count = 0

print(f'Total votes received by candidates : {total_votes}')
fifty_percent = math.ceil(total_votes / 2)
won = -1
highest, runnerup = 0, 0
print(total_votes_list)
for max_count in total_votes_list:
    if highest < max_count:
        highest = max_count
    if max_count >= fifty_percent:
        won = max_count
second_max = total_votes_list[0]
for second in total_votes_list:
    if second > second_max and second_max < max_count:
        second_max = second
if won > 0:
    print(f'Mayor {total_votes_list.index(won)} won the elections.')
else:
    print(f'Run-off between two candidates : {total_votes_list.index(second_max)} and {total_votes_list.index(highest)}.')

f.close()
