def remove_nth_element(temp_list, k):
    temp_list.remove(temp_list[k-1])
    if __name__ == '__main__':
        print(temp_list[:k] + temp_list[k:])


original_list = ['a', 'b', 'c', 'd']
if __name__ == '__main__':
    remove_nth_element(original_list, 2)
    print(original_list)
