def PenjadwalanPelanggan(n, himp):
    i = 0
    himp.sort()
    print()

    for item in himp:
        print(item, end=" ")
    print()
    
    for i in range(n):
        print(f"Pelanggan {i+1} dilayani!")

n = int(input())
himp = list(map(int, input().split()))
PenjadwalanPelanggan(n, himp)