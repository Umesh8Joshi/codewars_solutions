def duplicate_count(text):
    text = text.lower()
    ls,cnt = list(text),0
    my_dict = {i:ls.count(i) for i in ls}
    for x in my_dict.values():
        if x > 1:
            cnt += 1
    return cnt

if __name__ == "__main__":
    print(duplicate_count("Ummesh"))

'''
    def duplicate_count(s):
        return len([c for c in set(s.lower()) if s.lower().count(c)>1])
'''