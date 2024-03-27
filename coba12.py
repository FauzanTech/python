jumlah_data = int(input())
kumpulan_data = list(map(int, input().split()))
for i in range(len(kumpulan_data)):
    for j in range(i+1, len(kumpulan_data)):
        if kumpulan_data[i] > kumpulan_data[j]:
            kumpulan_data[i], kumpulan_data[j] = kumpulan_data[j], kumpulan_data[i]

for data in kumpulan_data:
    print(data, end=" ")