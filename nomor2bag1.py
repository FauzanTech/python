def PenjadwalanPelanggan(himp):
    i = 0
    result = []

    while len(himp) != 0:
        i = min(himp)
        himp.remove(i)
        result.append(i)

    print(result)


himpPelanggan = list(map(int, input().split()))
PenjadwalanPelanggan(himpPelanggan)