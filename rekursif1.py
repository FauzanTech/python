def generatePermutasi(current, digunakan, n, k, hasil):
    if len(current) == n:
        hasil.append(current[:])
        return
    
    for i in range(1, n+1):
        if not digunakan[i-1] and (not current or abs(current[-1]-i) <= k):
            digunakan[i-1] = True
            current.append(i)
            generatePermutasi(current, digunakan, n, k, hasil)
            current.pop()
            digunakan[i-1] = False


n, k = map(int, input().split())
digunakan = [False] * n
hasil = []
generatePermutasi([], digunakan, n, k, hasil)
# for num in hasil:
#     print(" ".join(map(str, num)))

    