original_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
first_part = []
second_part = []


def split_list_two_parts(source_list, count):
    first_part.append(source_list[:count])
    second_part.append(source_list[count:])
    return first_part + second_part


print(split_list_two_parts(original_list, 4))
