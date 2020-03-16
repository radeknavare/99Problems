from list_prime_39 import prime_list


def goldbach_conj(number, result_list=False):
    prime_pair_list = []
    l = prime_list(1, number)
    for i in range(0, len(l)):
        for j in range(1, len(l)):
            if l[i] + l[j] == number:
                if result_list:
                    prime_pair_list.append([l[i], l[j]])
                else:
                    return [l[i], l[j]]
    return prime_pair_list


if __name__ == '__main__':
    print(goldbach_conj(200, True))
