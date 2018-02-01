from functools import reduce
import numpy as np

def rang(lst):
    lst = lst[::]
    tmin, tmax = lst[0], lst[0]
    if len(lst) % 2 != 0:
        lst.append(lst[0])
    for i,j in zip(lst[0::2],lst[1::2]):
        try:
            int(i)
            int(j)
        except ValueError:
            return False
        if i < j:
            tmin = min(tmin, i)
            tmax = max(tmax, j)
        else:
            tmin = min(tmin, j)
            tmax = max(tmax, i)
    return tmax - tmin
def product(lst):
    return reduce(lambda x,y: x*y, lst)
def calc(lst):
    avg = np.average(lst)
    rng = rang(lst)
    med = np.median(lst)
    return rng, avg, med
def part(n):
    def partition(n):
        if n == 0:
            yield []
            return
        for p in partition(n-1):
            yield [1] + p
            if p and (len(p) <  2 or p[1] > p[0]):
                yield [p[0] + 1] + p[1:]
    prods = {product(p) for p in partition(n)}
    r, a, m = calc(list(prods))
    return "Range: {0} Average: {1:.2f} Median: {2:.2f}".format(r,a,m)