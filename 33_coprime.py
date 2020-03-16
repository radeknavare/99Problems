from Determine_the_greatest_common_divisor_of_two_positive_integer_numbers_32 import gcd

def coprime(num1, num2):
    if gcd(num1, num2) == 1:
        print("Co-Prime")
    else:
        print("Not Co-prime")


coprime(35, 64)
