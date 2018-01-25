def dup(arr):
    for a in arr:
        b = list(a)
        for x in range(len(b)):
            while x < len(b):
                if b[x] == b[x+1]:
                    print("yes")

if __name__ == "__main__":
    arr = ["ummmm", "mme"]
    dup(arr)