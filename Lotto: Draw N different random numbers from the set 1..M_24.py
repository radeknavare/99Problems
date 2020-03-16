import random

def random_nos_from_range(nos, limit):
    newlist = []
    for i in range(nos):
        newlist.append(random.randrange(1, limit, 1))
    return newlist



if __name__ == '__main__':
    print(random_nos_from_range(5, 99))
