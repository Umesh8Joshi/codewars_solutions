import functools
def gcd(a,b):
    while(b):
        a, b = b, a%b
    return a

def lcm(a,b):
    return a*b // gcd(a,b)

def lcmm(*args):
    return functools.reduce(lcm, args)

def converFracts(lst):
    ls,lcms = [], 0
    for x in lst:
        ls.append(x[1])
    for i in range(len(ls)-1):
        lcms = lcmm(ls[i],ls[i+1])
    for x in lst:
        x[0] = int(lcms/x[1])
        x[1] = lcms
    return lst
if __name__ == "__main__":
    converFracts([[1, 2], [1, 3], [1, 4]])


'''
    from fractions import gcd

def get_lcm(lst):
  return reduce(lambda x, y : x*y/gcd(x,y), lst)

def convertFracts(lst):
  lcm = get_lcm([ y for x, y in lst])
     return [ [x*lcm/y, lcm] for x, y in lst]
'''