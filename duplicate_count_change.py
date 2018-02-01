def duplicate_encode(word):
    word = word.lower()
    rtn = {}
    ans = []
    my_dict = {i: word.count(i) for i in word}
    for x in my_dict.keys():
        if my_dict[x] == 1:
            rtn[x] = "("
        else:
            rtn[x] = ")"
    for y in list(word):
        ans.append(rtn[y])
    return ''.join(ans)

if __name__ == "__main__":
    print(duplicate_encode("Umm"))