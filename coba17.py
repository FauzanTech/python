# baris, kolom > 1
# baris, kolom = list(map(int, input().split()))

# if kolom == 1:
#     print(baris-kolom)
# else:
#     print((kolom-1)*baris

# patung = int(input())
# tinggi_patung = list(map(int, input().split()))
# import numpy as np
A, B = list(map(int, input().split()))
def fpb(a, b):
    if b == 0:
        return a
    else:
        return fpb(b, a%b)

def kpk(a, b):
    return int(a/fpb(a, b))*b

print(kpk(A, B))
# # x = 1
# # y = 1
# # keliA = A * x 
# # keliB = B * y

# # while keliA != keliB:
# #     while keliA > keliB:
# #         y += 1
# #         keliB = B * y
# #     while keliA < keliB:
# #         x += 1
# #         keliA = A * x

# print(np.lcm(A, B))