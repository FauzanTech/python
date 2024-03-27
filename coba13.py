# komik = int(input())
# jilid = list(map(int, input().split()))
# waktu = 0

# for i in range(komik):
#     if jilid[i] == min(jilid):
#         continue
#     for j in range(i+1, komik):
#         if jilid[i] > jilid[j]:
#             jilid[i], jilid[j] = jilid[j], jilid[i]
#             waktu += 1

# print(waktu)
# n = 6
# arr = [-4, 3, -9, 0, 4, 1]

# postive = 0
# negative = 0
# zero = 0

# for num in arr:
#     if num >

# waktu = input()

# def timeConversion(s):
#     # Write your code here
    
#     if s[-2:].lower() == "PM".lower():
#         if s[:2] == "12":
#             return s[:-2]
        
#         x = s[:2]
#         ubah = str(int(x) + 12)
#         return ubah + s[2:-2]
    
#     if s[-2:].lower() == "AM".lower():
#         if s[:2] == "12":
#             ubah = "0" + str(int(s[:2])-12)
#             return ubah + s[2:-2]
        
#         return s[:-2]
    
# print(timeConversion(waktu))

# a = [2, 4]
# b = [16, 32, 96]
# angka = [i for i in range(a[-1], b[0]+1)]

# print(angka)
# lis1 = []
# kondisi = False
# for num in angka:
#     for j in range(len(a)):
#         if num%a[j] == 0:
#             kondisi = True
#         else:
#             kondisi = False

#         if j == len(a)-1 and kondisi == True:
#             lis1.append(num)
    
# print(lis1)
# result = []
# kondisi = False
# for num in lis1:
#     for j in range(len(b)):
#         if b[j]%num == 0:
#             kondisi = True
#         else:
#             kondisi = False
#             break

#         if j == len(b)-1 and kondisi == True:
#             result.append(num)

# print(result)
# print(len(result))

# lis2 = []
# for i in a:
#     for num in angka:
#         if num%i == 0:
#             lis2.append(num)

# print(lis2)

# total_test = int(input())
# jumlah_batu = [int(input()) for _ in range(total_test)]

# player1 = 0
# player2 = 0

# for batu in jumlah_batu:
#     if batu < 2 or batu == 7:
#         print("second")
d = 3
m = 2
s = [1, 2, 1, 3, 2]
arr1 = []
awal = 0
akhir = m
while True:
    arr1.append(s[awal:akhir])
    akhir += m-1
    awal += 1
    
    if akhir >= len(s):
        break

print(arr1)
result = []
for item in arr1:
    if sum(item) == d:
        result.append(item)

print(result)