duplicate_elements_list = ['a', 'b', 'c', 'a', 'b', 'a', 'a', 'b', 'c', 'd', 'e', 'f', 'd']
duplicate_elements_list.sort()
pointer = 0
tempList = []
newList = []
while 1:
    tempList += (duplicate_elements_list.count(duplicate_elements_list[pointer]) * duplicate_elements_list[pointer])
    newList.append(tempList)
    pointer += duplicate_elements_list.count(duplicate_elements_list[pointer])
    tempList = []
    if pointer >= len(duplicate_elements_list):
        break
print(newList)
