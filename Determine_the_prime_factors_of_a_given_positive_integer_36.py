from prime_factors_35 import prime_factor

l = prime_factor(10)
print(l)
newList = []


def prime_factors_length_encoding(l=[]):

    prev_item = l[0]
    cnt = 0
    for item in l:
        # if l.count(item) == 1:
        #     newList.append([item, 1])
        # else:
        if item == prev_item:
            cnt += 1
        else:
            newList.append([prev_item, cnt])
            prev_item = item
            cnt = 1
    newList.append([item, cnt])
    return newList


if __name__ == '__main__':
    prime_factors_length_encoding(l)
    print(newList)
