pendaftar, antri = list(map(int, input().split()))
kumpulanPendaftar = [input() for _ in range(pendaftar)]
antrian = [input() for _ in range(antri)]

for orang in antrian:
    if orang in kumpulanPendaftar:
        print(kumpulanPendaftar.index(orang)+1)
    else:
        print(-1)