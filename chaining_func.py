def f1(x):
    return x*2
def f2(x):
    return x+2
def f3(x):
    return x**2
def f4(x):
    return s.split(x)
def f5(xs):
    return [x[::-1].title() for x in xs]
def f6(xs):
    return "_".join(xs)

def chained(functions):
    for function in functions:
        return function()