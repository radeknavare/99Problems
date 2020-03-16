import itertools


def eval_log_exp(exp):
    newstr = []
    l = [True, False]
    keys = exp.replace('(', '').replace(')', '').replace('and', '').replace('or', '').split(' ')
    newset = set(keys)
    newset.remove('')
    keys = list(newset)
    keys.sort()
    var_count = len(keys)

    total_permutation = list(itertools.product(l, repeat=var_count))

    for values in total_permutation:
        res = {keys[i]: values[i] for i in range(0, var_count)}
        print(res)
        new = exp
        values1_str = ''
        for keys1, values1 in res.items():
            new = new.replace(keys1, str(values1))
            values1_str += str(values1) + '\t'
        print(f'{values1_str}{eval(new)}')


eval_log_exp("A and (E or (C and (A or B) and D or E) and R)")
