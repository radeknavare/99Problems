duplicate_elements_list = ['a', 'b', 'c', 'a', 'b', 'a', 'a', 'b', 'c', 'd', 'e', 'f', 'd']
duplicate_elements_list.sort()
pointer = 0
tempList = []
newList = []

prev_item = duplicate_elements_list[0]
cnt = 0
for item in duplicate_elements_list:

    if item == prev_item:
        cnt += 1
    else:
        if cnt == 1:
            newList.append(str(prev_item))
            prev_item = item
        else:
            newList.append(list((str(prev_item) + " " +str(cnt)).split(",")))
            prev_item = item
            cnt = 1
            tempList = []
newList.append(list((str(prev_item) + " " + str(cnt)).split(",")))
print(newList)
