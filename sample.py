
def rec(a):
    if a==1 or a==2:
        return 1
    else:
        return rec(a-1)+rec(a-2)
print(rec(50))