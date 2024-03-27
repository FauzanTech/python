baris, kolom, ikan, percobaan = list(map(int, input().split()))
petak = [list(input()) for _ in range(baris)]
kumpulan_percobaan = [list(map(int, input().split())) for _ in range(percobaan)]

jarak = 0
for i in range(baris):
    for j in range(len(kumpulan_percobaan)):
        benda = kumpulan_percobaan[j]
        for _ in range(benda[1]):
            if petak[i].index("X") == benda[1]-benda[1]:
                jarak += 1
            elif petak[i].index("X") == benda[1]:
                jarak += 1
        

print(jarak)