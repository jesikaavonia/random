def cycle(l):
    if len(l)==0:
        return
    a=l[0]
    del l[0]
    l.append(a)
    return l

list=[1,2,3,4,'d']

print(list)
cycle(list)
print(list)
