run_length_encoded_list = [['a 4'], ['b 3'], ['c 2'], ['d 2'], 'e', ['f 1']]
newList = []


def recursive_decompress_list(compressed_list):

    for item in compressed_list:
        if type(item) == list:
            split_string = item[0].split(" ")
            for i in range(int(split_string[1])):
                newList.append(split_string[0])
        else:
            newList.append(item)


recursive_decompress_list(run_length_encoded_list)
print(newList)
