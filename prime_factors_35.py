import math
from Determine_whether_a_given_integer_number_is_prime_31 import isprime

def prime_factor(number):
    l = []
    while number % 2 == 0:
        number = int(number/2)
        l.append(2)
        if __name__ == '__main__':
            print(2)

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            if __name__ == '__main__':
                print(i)
            l.append(i)
            number = int(number / i)

    if number > 2:
        l.append(number)
        if __name__ == '__main__':
            print(number)
    return l


# def prime_factor(number):
#     i = 2
#     temp = number
#     print(isprime(number))
#     # if isprime(number):
#     #     print(number)
#     while i <= temp/2:
#         if number % i == 0:
#             number /= i
#             print(i)
#         else:
#             i += 2

if __name__ == '__main__':
    prime_factor(10)
