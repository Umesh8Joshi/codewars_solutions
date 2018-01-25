def gap(g,m,n):
    ls = []
    for i in range(m,n+1):
        if all(i % j for j in range(2,i)):
            ls.append(i)
    diff = [x -ls[i-1] for i,x in enumerate(ls)][1:]
    for a in range(0,len(diff)):
        if diff[a] == g:
            return [ls[a], ls[a+1]]
            continue
    return None

if __name__ == "__main__":
    gap(1,100,110)