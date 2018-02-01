from itertools import permutations

def solve(s):
    ls = permutations(s)
    print(ls)
    return ls

if __name__ == "__main__":
    print(solve([1,2]))