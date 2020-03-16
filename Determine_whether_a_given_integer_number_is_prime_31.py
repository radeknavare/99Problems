def isprime(number):

    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    if isprime(17):
        print("prime number")
    else:
        print("Not prime")
