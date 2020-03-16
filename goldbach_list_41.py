from goldbach_conjecture_40 import goldbach_conj


def goldbach_list(lower, upper):
    for i in range(lower, upper+1):
        if i % 2 == 0:
            print(goldbach_conj(i))
    print([f'{i} = {goldbach_conj(i)}' for i in range(lower, upper+1) if i % 2 == 0])

goldbach_list(9, 20)