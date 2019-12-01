import random

# Miller-Rabin Primality Test
def primarity_test(text, k):
    response_string = ''
    index_st = text.find(' ')
    index_ed = text.find('は素数')
    q = int(text[index_st:index_ed])
    if q == 2:
        response_string = str(q) + 'は **素数** です！'
        return response_string
    if q < 2 or q & 1 == 0:
        response_string = str(q) + 'は **素数じゃない** です！'
        return response_string

    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, q-1)
        t = d
        y = pow(a, t, q)
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q-1 and t & 1 == 0:
            response_string = str(q) + 'は **素数じゃない** です！'
            return response_string
        response_string = str(q) + 'は **素数** です！'
    return response_string

