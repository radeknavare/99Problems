from Determine_the_greatest_common_divisor_of_two_positive_integer_numbers_32 import gcd

def euler_toitent(m):
    cnt = 0
    for i in range(1, m):
        if gcd(m, i) == 1:
            cnt += 1
    return cnt

print(f'Euler\'s toitent is : {euler_toitent(16)}')
