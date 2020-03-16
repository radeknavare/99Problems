duplicate_list = [1, 2, 3, 1, 2, 5, 6, 6, 3, 4, 8, 5]
unique_list = []
print(list(dict.fromkeys(duplicate_list)))
for i in duplicate_list:
    if i in unique_list:  # unique_list.count(i) == 1:
        continue
    else:
        unique_list.append(i)
else:
    print("Else after for loop")

print(unique_list)
