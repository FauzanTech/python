baris, kolom = list(map(int, input().split()))

for i in range(baris):
    print("*"*kolom)

# maze = [
#     [[],[]],
#     [[],[]],
#     [[],[]]
# ]

# for i in range(baris):
#     for j in range(kolom):
#         if maze[i][j] == []:
#             maze[i][j] = 1

start = [1,1]
jumlah_jalanKeluar = []
def cariJalanKeluar(posisi):
    global jumlah_jalanKeluar
    if posisi == [baris,kolom]:
        jumlah_jalanKeluar.append(1)
        return 
    else:
        if posisi[0] < baris:
            posisi[0] += 1
            cariJalanKeluar(posisi)
            if posisi[1] < kolom:
                posisi[1] += 1
                cariJalanKeluar(posisi)
        elif posisi[1] < kolom:
            posisi[1] += 1
            cariJalanKeluar(posisi)
            if posisi[0] < baris:
                posisi[0] += 1
                cariJalanKeluar(posisi)

cariJalanKeluar(start)
print(len(jumlah_jalanKeluar))