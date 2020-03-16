duplicate_elements_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
n = 3
# del duplicate_elements_list[n-1::n]
print(duplicate_elements_list)
new_list = [item for index, item in enumerate(duplicate_elements_list) if (index + 1) % n]
print(new_list)
