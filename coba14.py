perintah = int(input())
nama_pengantri = []

for _ in range(perintah):
    stdin = input().split()
    if stdin[0] == "2":
        nama_pengantri.append(stdin[1])
    elif stdin[0] == "1":
        nama_pengantri.insert(0, stdin[1])    
    elif stdin[0] == "3":
        print(nama_pengantri.pop(0))
    else:
        print(nama_pengantri.pop())
