'''
    check if the given range contains some double prime or not
    13 and 17 are double prime as 31 and 71 are also prime
'''

def is_prime(a):
    return all(a % i for i in range(2, a))
def is_back_prime(c):
    b = int(str(c)[::-1])
    return is_prime(b)
def backwardsPrime(start,stop):
    ls = []
    if start < 10: start = 10
    for i in range(start, stop):
        if is_prime(i) and is_back_prime(i):    ls.append(i)
    return ls
print(backwardsPrime(2, 1000))

'''
    # passed every code
'''