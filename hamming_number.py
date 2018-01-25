from itertools import tee, islice

def times(n, generator):
    for i in generator:
        yield n * i

def merge(gen1, gen2):
    ngen1 = gen1.next()
    ngen2 = gen2.next()
    while 1:
        if ngen1 < ngen2:
            yield ngen1
            ngen1 = gen1.next()
        elif ngen2 < ngen1:
            yield ngen2
            ngen2 = gen2.next()
        else:
            yield ngen1
            ngen1 = gen1.next()
            ngen2 = gen2.next()

def hamming(n):
    def _hamming():
        yield 1
        for n in merge(times(2, m2), merge(times(3, m3), times(5, m5))):
            yield n
    m1 = _hamming()
    m2, m3, m5, mres = tee(m1, 4)
    return next(islice(mres, n-1, None), None)


assert hamming(1) == 1
assert hamming(2) == 2
assert hamming(3) == 3
assert hamming(4) == 4
assert hamming(5) == 5
assert hamming(6) == 6
assert hamming(7) == 8
assert hamming(8) == 9
assert hamming(9) == 10
assert hamming(10) == 12
assert hamming(11) == 15
assert hamming(12) == 16
assert hamming(13) == 18
assert hamming(14) == 20
assert hamming(15) == 24
assert hamming(16) == 25
assert hamming(17) == 27
assert hamming(18) == 30
assert hamming(19) == 32
print('ok')