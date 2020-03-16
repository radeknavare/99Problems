original_list = ['a', 'b', 'c', 'c', 'd']
duplicate_list = []


def replicate_list_items(original_list, count):

    for item in original_list:
        duplicate_list.append(item * count)
    return duplicate_list


replicate_list_items(original_list, 2)
print(duplicate_list)
