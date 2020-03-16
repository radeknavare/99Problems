# Find the last box of a list.

nameList = ["Kedar", "Rahul", "Shashank", "Vivek"]

print("Using length - 1 : " + nameList[len(nameList)-1])
print("Using -1 index : " + nameList[-1])

# This method deletes the popped element

print("Using pop() : " + nameList.pop(-1))
print("Popped element deleted from List : " + str(nameList))
nameList.append("Vivek")

print("Using reversed and next function : " + next(reversed(nameList)))

# Find the last but one box of a list.

print("Second last element : " + nameList[-2])


