def seleksi(x, batas):
    nilai_awal = x
    jumlah_koin = []
    i = 1
    while nilai_awal*i <= batas:
        x=nilai_awal*i
        i+=1
        jumlah_koin.append(nilai_awal)

    batas-=x
    return x, nilai_awal, batas, jumlah_koin

def greedy(himp, batas):
    batas_tetap = batas
    jumlah_koin = []
    solusi = []

    while len(himp) != 0:
        if sum(solusi)+max(himp) <= batas_tetap:
            x, nilai_awal, batas, penambahan_koin = seleksi(max(himp), batas)
            himp.remove(nilai_awal)
            solusi.append(x)
            jumlah_koin+=penambahan_koin
            if sum(solusi) == batas_tetap:
                break
        else:
            himp.remove(max(himp))
        
    if sum(solusi) == batas_tetap:
        print("solusi ditemukan")
        print(f"{solusi} = {batas_tetap}")
        print(f"{jumlah_koin} = {len(jumlah_koin)} koin")
    else:
        print("tidak ada solusi")


himp = list(map(int, input("Masukkan jenis koin ").split()))
jumlah_koin = int(input("Masukkan jumlah koin "))
greedy(himp, jumlah_koin)