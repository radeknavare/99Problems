newList = [1, 2, 3, 2, 1]
newTuple = (1, 2, 3, 2, 1)
if newTuple == newTuple[::-1]:
    print("Palindrome")

else:
    print("Not Palindrome")

if newList == newList[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
