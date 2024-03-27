bil = int(input())

def fk(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fk(n-1)

bars = fk(2)
total_slot = fk(bil+2)
print(int(total_slot/(bars*fk(bil))))