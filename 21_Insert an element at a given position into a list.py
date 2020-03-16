def insert_at_pos(temp_list, value, pos):
    # temp_list.insert(pos-1, value)
    return temp_list[:pos-1] + [value] + temp_list[pos-1:]


original_list = ['a', 'b', 'c', 'd']
original_list = insert_at_pos(original_list, 'e', 2)
print(original_list)
