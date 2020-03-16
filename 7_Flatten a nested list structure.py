nestedList = [1, 2, [3, 4], 5, [6, 7]]
flattened_list = []


def flatten_list(nested_list):
    for item in nested_list:
        if type(item) == list:
            flatten_list(item)
        else:
            flattened_list.append(item)


flatten_list(nestedList)
print(flattened_list)
