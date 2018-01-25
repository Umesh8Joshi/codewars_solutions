def trailingZero(n):
    count = 0
    i = 5
    while (n/i >= 1):
        count += n/i
        i *= 5
    return int(count)
if __name__ == "__main__":
    print(trailingZero(12))
