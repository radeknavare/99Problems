from Determine_the_prime_factors_of_a_given_positive_integer_36 import prime_factors_length_encoding, prime_factor

l = prime_factor(10)
l = prime_factors_length_encoding(l)
print(l)
m = 0

for item in l:
    m += (item[0] - 1) * item[0] ** (item[1] - 1)

print(m)
