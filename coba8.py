panjangSekuens = int(input())
elemenSekuens = list(map(int, input().split()))
result = 0

for i in range(panjangSekuens):
    for j in range(i+1, panjangSekuens):
        if i < j and elemenSekuens[i] > elemenSekuens[j]:
            result += 1

print(result)