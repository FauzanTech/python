# jumlah_pertanyaan = int(input())
# antrian = []
# for _ in range(jumlah_pertanyaan):
#     inp = input().split()
#     if inp[0] == "DAFTAR":
#         antrian.append(inp[1])
#     else:
#         print(antrian.count(inp[1]))
# list1 = [i for i in range(1, 13)]
# print(list1)
# print(list1[int(len(list1)/2)])
# print((list1[int(len(list1)/2)-1]+list1[int(len(list1)/2)])/2)
import statistics
from decimal import Decimal
bil = int(input())

for i in range(bil):
    print(Decimal(statistics.median(input())).normalize())
    # data.sort()
    # if len(data)%2 != 0:
    #     print(data[int(len(data)/2)])
    # else:
    #     if ((data[int((len(data)/2)-1)]) + (data[int((len(data)/2))])) %2 != 0: 
    #         print((data[int((len(data)/2)-1)] + data[int((len(data)/2))])/2) 
    #     else:    
    #         print(int((data[int((len(data)/2)-1)] + data[int((len(data)/2))])/2)) 