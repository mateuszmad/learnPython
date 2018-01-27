
def fibonacci(x):
    flist = []
    f0 = 0
    f1 = 1
    for i in range(1,x+1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
        flist.append(f2)
    return flist
