def gcd(first, second):
    if first == 0:
        return second

    return gcd(second % first, first)

    # while first != second:
    #     if first == 1 or second == 1:
    #         return 1
    #     if first > second:
    #         first -= second
    #     second -= first
    # return first


if __name__ == '__main__':
    print(gcd(81, 153))