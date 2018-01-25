def delete_nth(order,max_e):
    d = {x:order.count(x) for x in order}
    print(d)
    for z in d.values():
        if z > max_e:
            print(z)
if __name__ == "__main__":
    delete_nth([1,2,3,3,4,5,1,1],2)