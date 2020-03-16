l=[]


def list_given_range(start, end):
    for i in range(start, end+1):
        l.append(i)
    return l


print(list_given_range(4, 9))