jumlah_kata = int(input())
kumpulan_kata = [input() for i in range(jumlah_kata)]

def cek(kata):
    listHuruf = list(kata)
    listHuruf.reverse()
    if kata == "".join(listHuruf):
        print("palindrom")
    else:
        print("bukan palindrom")

for i in kumpulan_kata:
    cek(i)