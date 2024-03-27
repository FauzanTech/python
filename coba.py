# stdin = int(input())
# arr = [1]

# for i in range(2, stdin+1):
#     faktor_bilangan = 0
#     for j in range(1, i+1):
#         if i%j == 0:
#             faktor_bilangan += 1

#     arr.append(faktor_bilangan)

# print(sum(arr))

# stdin = int(input())
# harga = list(map(int, input().split()))
# for i in range(1, stdin+1):
#     for j in range(i+1, stdin+1):
#         if harga[i-1] > harga[j-1]:
#             harga[i-1], harga[j-1] = harga[j-1], harga[i-1]
#             print(i, j)

# abcde
# bacde
# edcab

string = "abcde"
string = string[1:]
string = list(string)
string.reverse()
string = "".join(string)
print(string)

# string[0], string[1] = string[1], string[0]
# print("".join(string))


