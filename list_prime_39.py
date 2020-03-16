from Determine_whether_a_given_integer_number_is_prime_31 import isprime


def prime_list(lower, upper):
    prime_nos_list = []
    for number in range(lower, upper+1):
        if isprime(number):
            prime_nos_list.append(number)
    return prime_nos_list


if __name__ == '__main__':
    print(prime_list(1, 100))
