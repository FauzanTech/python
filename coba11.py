banyak_badak, banyak_pertanyaan = map(int, input().split())
cula = list(map(int, input().split()))
cula.sort()
kumpulan_pertanyaan = [int(input()) for _ in range(banyak_pertanyaan)]

for index in kumpulan_pertanyaan:
    print(cula[index-1])