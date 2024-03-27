baris, kolom, ikan, percobaan = map(int, input().split())

lokasi_ikan = []
total_ikan = 0
for i in range(baris):
    petak = input()
    if "X" not in petak:
        continue
    elif total_ikan == ikan:
        break

    for j in range(kolom):
        if petak[j] == "X":
            lokasi_ikan.append((i+1,j+1))
            total_ikan += 1

def jarak_manhattan(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def langkah_terdekat(lokasi, x2, y2):
    arrjarak = []
    for x1, y1 in lokasi:
        jarak = jarak_manhattan(x1, y1, x2, y2)
        arrjarak.append(jarak)
    return min(arrjarak)

result = []
for _ in range(percobaan):
    x2, y2 = map(int, input().split())
    result.append(langkah_terdekat(lokasi_ikan, x2, y2))
    
for langkah in result:
    print(langkah)