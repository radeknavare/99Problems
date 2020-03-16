import random

def extract_random_elements_limit(nos, l=[]):
    newlist = []
    while nos > 0:
        rand_value = l[random.randrange(0, len(l), 1)]
        if newlist.count(rand_value) == 0:
            newlist.append(rand_value)
            nos -= 1
    return newlist


if __name__ == '__main__':
    print(extract_random_elements_limit(3, ['3', '4', '2', '0', '5', '12', '34', '53']))
