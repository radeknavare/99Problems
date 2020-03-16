original_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
limit = -2

# del original_list[:limit]
print(original_list[limit:] + original_list[:limit])
