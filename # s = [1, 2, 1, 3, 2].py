# s = [1, 2, 1, 3, 2]
# d = 3
# m = 2

# s = list(map(int, input().split()))
# d, m = list(map(int, input().split()))


# indexAwal = 0
# indexAkhir = m
# kumpulan_list = []

# while indexAkhir <= len(s):
#     if sum(s[indexAwal:indexAkhir]) == d:
#         kumpulan_list.append(s[indexAwal:indexAkhir])
#     indexAwal += 1
#     indexAkhir += 1

# print(len(kumpulan_list))

arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]

arr1 = set(arr)
arr1 = list(arr1)
arr2 = []
for i in arr1:
    arr2.append(arr.count(i))

result = 0
for j in arr2:
    if j%2 == 0:
        result += int(j/2)
    else:
        result += int((j-1)/2)

print(arr)
print(result)

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if not arr1 or arr1[i] == 
# arr1.append((arr[i], arr.count(arr[i])))
