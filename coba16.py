jumlah_pemain, power_musuh = map(int, input().split())
power_kita = list(map(int, input().split()))

print(power_kita)
for i in range(jumlah_pemain):
    print("Perulangan i:",i)
    for j in range(i+1, jumlah_pemain):
        print("Perulangan j:", j)


# new = []
# for i in range(jumlah_pemain):
#     for j in range(jumlah_pemain):
#         if power_kita[i] > power_musuh:
#             new.append([power_kita[i]])
#             power_kita.pop(i)
#         else:
#             new2 = []
#             while power_kita < power_musuh:
#                 new2.append(power_kita[i])
#                 new2.append(power_kita[j])
#                 power_kita[i] += power_kita[j]
#             print(new2)

