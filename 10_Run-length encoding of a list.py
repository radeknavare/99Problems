duplicate_elements_list = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
#duplicate_elements_list.sort()
#pointer = 0
#tempList = []
newList = []
# while 1:
#    tempList += str((duplicate_elements_list[pointer])) + str(duplicate_elements_list.count(duplicate_elements_list[pointer]))
#    newList.append(tempList)
#    pointer += duplicate_elements_list.count(duplicate_elements_list[pointer])
#    tempList = []
#    if pointer >= len(duplicate_elements_list):
#        break
#print(newList)
#newList =[]
prev_item = duplicate_elements_list[0]
cnt = 0
for item in duplicate_elements_list:

    if item == prev_item:
        cnt += 1
    else:
        newList.append(list((str(prev_item) + " " + str(cnt)).split(",")))
        prev_item = item
        cnt = 1
        tempList = []
newList.append(list((str(prev_item) + " " + str(cnt)).split(",")))
print(newList)
